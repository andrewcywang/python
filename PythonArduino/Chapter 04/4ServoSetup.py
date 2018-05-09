from pyfirmata import Arduino
from pyfirmata import SERVO
from time import sleep

# Setting up the Arduino board
port = 'COM3'
board = Arduino(port)
# Need to give some time to pyFirmata and Arduino to synchronize
sleep(5)

# 設定底座，左邊，右邊，鉗爪的 pin
pinBottom, pinLeft, pinRight, pinHand = 9, 10, 11, 6
bAngle, lAngle, rAngle, hAngle = 75, 90, 60, 0

# Custom angle to set Servo motor angle
def setServoAngle(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

board.digital[pinBottom].mode = SERVO
setServoAngle(pinBottom, bAngle)
board.digital[pinLeft].mode = SERVO
setServoAngle(pinLeft, lAngle)
board.digital[pinRight].mode = SERVO
setServoAngle(pinRight, rAngle)
board.digital[pinHand].mode = SERVO
setServoAngle(pinHand, hAngle)

def initPos():
    setServoAngle(pinBottom, bAngle)
    setServoAngle(pinLeft, lAngle)
    setServoAngle(pinRight, rAngle)
    setServoAngle(pinHand, hAngle)

print('搖頭三次:')
curBtmAngel = bAngle
for s in range(3):
    for i in range(curBtmAngel, curBtmAngel-60, -1):
        setServoAngle(pinBottom, i)
    curBtmAngel = curBtmAngel - 60

    for i in range(curBtmAngel, curBtmAngel+120):
        setServoAngle(pinBottom, i)
    curBtmAngel = curBtmAngel + 120

    for i in range(curBtmAngel, curBtmAngel-60, -1):
        setServoAngle(pinBottom, i)
    curBtmAngel = curBtmAngel - 60
    
    print('底盤角度',curBtmAngel)

print('抬頭三次')
curLftAngle = lAngle
for s in range(3):
    for i in range(curLftAngle, curLftAngle+60):
        setServoAngle(pinLeft, i)
    curLftAngle = curLftAngle + 60
    for i in range(curLftAngle, curLftAngle-60,-1):
        setServoAngle(pinLeft, i)
    curLftAngle = curLftAngle - 60
    print('高低角度',curLftAngle)


board.exit()

