from pyfirmata import Arduino
from time import sleep

# Setting up the Arduino board
port = 'COM4'
board = Arduino(port)
# Need to give some time to pyFirmata and Arduino to synchronize
sleep(3)
d7 = board.get_pin('d:7:o')
d6 = board.get_pin('d:6:o')

# Running loop for ever
# This command executes loop body indefinitely until keyboard interrupt

try:
    d6.write(1)
    d7.write(0)
except KeyboardInterrupt:
    board.exit()

