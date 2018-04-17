from pyfirmata import Arduino
from time import sleep

pin = 8
pin2 = 9
port = 'COM3'
board = Arduino(port)

for i in range(100):
    board.digital[pin].write(0)
    board.digital[pin2].write(1)
    time.sleep(1)
    board.digital[pin].write(1)
    board.digital[pin2].write(0)
    sleep(1)
