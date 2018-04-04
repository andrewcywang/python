from pyfirmata import Arduino
from time import sleep

port = 'COM3'
board = Arduino(port)

def off_light(x):
    board.digital[x].write(1)

def off_all():
    for i in range(2,10):
        off_light(i)

off_all()

def on_light(x):
    board.digital[x].write(0)

def on_all():
    for i in range(2,10):
        on_light(i)

circle = [2, 3, 4, 5, 6, 7]
for x in range(3):
    for i in circle:
        on_light(i)
        sleep(0.2)
        off_all()

for x in range(3):
    on_all()
    sleep(0.2)
    off_all()
    sleep(0.2)

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
        board.digital[i+2].write(x[i])

for i in all_num:
    on_number(i)
    sleep(0.5)
    off_all()

na = [0,0,0,1,0,0,0]
nb = [1,1,0,0,0,0,0]
nc = [0,1,1,0,0,0,1]
nd = [1,0,0,0,0,1,0]
ne = [0,1,1,0,0,0,0]
nf = [0,1,1,1,0,0,0]
all_ltr = [na, nb, nc, nd, ne, nf]

for i in all_ltr:
    on_number(i)
    sleep(0.5)
    off_all()
