from pyfirmata import Arduino
from time import sleep

port = 'COM3'
board = Arduino(port)

digicontral = [10,11,12,13]
fontcontral = [3,4,5,6,7,8,9]

d0 = [1,0,0,0]  #第一個代表0，依序 1,2,3
d1 = [0,1,0,0]  #第一個代表0，依序 1,2,3
d2 = [0,0,1,0]  #第一個代表0，依序 1,2,3
d3 = [0,0,0,1]  #第一個代表0，依序 1,2,3
all_digit = [d0,d1,d2,d3]

def setd(x):
    for i in digicontral:
        board.digital[i].write(x[i-digicontral[0]])

def off_light(x):
    board.digital[x].write(1)
def off_all():
    for i in fontcontral:
        off_light(i)

def on_light(x):
    board.digital[x].write(0)
def on_all():
    for i in fontcontral:
        on_light(i)

for i in all_digit:
    setd(i)
    on_all()
    sleep(0.5)
    off_all()

n0 = [0,0,0,0,0,0,1]
n1 = [1,0,0,1,1,1,1]
n2 = [0,0,1,0,0,1,0]
n3 = [0,0,0,0,1,1,0]
n4 = [1,0,0,1,1,0,0]
n5 = [0,1,0,0,1,0,0]
n6 = [0,1,0,0,0,0,0]
n7 = [0,0,0,1,1,1,1]
n8 = [0,0,0,0,0,0,0]
n9 = [0,0,0,0,1,0,0]
all_num = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]

def on_number(x):
    for i in range(7):
        board.digital[i+3].write(x[i])

count=1  
for i in all_digit:
    setd(i)
    on_number(all_num[count])
    count += 1
    sleep(0.5)
    off_all()
    
na = [0,0,0,1,0,0,0]
nb = [1,1,0,0,0,0,0]
nc = [0,1,1,0,0,0,1]
nd = [1,0,0,0,0,1,0]
ne = [0,1,1,0,0,0,0]
nf = [0,1,1,1,0,0,0]
ng = [0,1,0,0,0,0,1]
nh = [1,0,0,1,0,0,0]
nj = [1,0,0,0,1,1,1]
nl = [1,1,1,0,0,0,1]
all_ltr = [na, nb, nc, nd, ne, nf, ng, nh, nj, nl]
halo = [nh, na, nl, n0]

count=0
for i in reversed(all_digit):
    setd(i)
    on_number(halo[count])
    count += 1
    sleep(0.5)
    off_all()

while True:
    count=0
    for i in reversed(all_digit):
        setd(i)
        on_number(halo[count])
        count += 1
        
