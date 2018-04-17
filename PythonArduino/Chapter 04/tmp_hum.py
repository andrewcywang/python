from pyfirmata import Arduino, util
from time import sleep

# Setting up the Arduino board
port = 'COM4'
board = Arduino(port)
# Need to give some time to pyFirmata and Arduino to synchronize
sleep(5)

# Start Iterator to avoid serial overflow
it = util.Iterator(board)
it.start()

# Assign a role and variable to analog pin 0 
a0 = board.get_pin('a:0:i')

# Running loop for ever
# This command executes loop body indefinitely until keyboard interrupt

try:
    while True:
        # Reading value on port a0
        p = a0.read()
        print(p)
        sleep(5)
except KeyboardInterrupt:
    board.exit()

