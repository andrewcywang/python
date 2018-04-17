#舵機校正

from pyfirmata import Arduino
from pyfirmata import SERVO
from time import sleep

# Setting up the Arduino board
port = 'COM3'
board = Arduino(port)
# Need to give some time to pyFirmata and Arduino to synchronize
sleep(5)

# 設定底座，左邊，右邊，鉗爪的 pin
pinBottom, pinLeft, pinRight, pinHand = 11, 10, 9, 6
board.digital[pinHand].mode = SERVO

# Custom angle to set Servo motor angle
def setServoAngle(pin, angle):
    board.digital[pin].write(angle)
    sleep(3)

# 實際設定角度 90, 90, 90, 25
setServoAngle(pinHand, 25)

board.exit()

