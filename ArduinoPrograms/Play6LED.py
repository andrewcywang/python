import pyfirmata
from time import sleep

led1, led2, led3, led4, led5, led6, led7, led8, p = 2, 3, 4, 5, 6, 7, 8, 9, 10
port = 'COM3'
board = pyfirmata.Arduino(port)


def style1():
    for i in range(led1, led8 + 1):
        board.digital[i].write(1)
        sleep(0.2)
    for i in range(led8, led1 - 1, -1):
        board.digital[i].write(0)
        sleep(0.2)

for i in range(1):
    style1()

last = 0
def note(x):
    global last
    for i in x:
        if last != 0:
            board.digital[last].write(0)
        if i != p:
            board.digital[i].write(1)
            sleep(0.4)
        else:
            sleep(0.4)
        board.digital[i].write(0)
        sleep(0.1)
        last = i
        
play1 = [led5, led3, led3, p, led4, led2, led2, p]
play2 = [led1, led2, led3, led4, led5, led5, led5, p]
play3 = [led1, led3, led5, led5, led3, led3, led3, p]
play4 = [led2, led2, led2, led2, led2, led3, led4, p]
play5 = [led1, led3, led5, led5, led1, led1, led1, p]

note(play1)
note(play2)
note(play1)
note(play3)
note(play4)
note(list(map(lambda x:x+1,play4[:7:]))+[p])
note(play1)
note(play5)



