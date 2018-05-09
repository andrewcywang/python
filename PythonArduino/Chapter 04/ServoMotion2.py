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
bAngle, lAngle, rAngle, hAngle = 75, 90, 90, 0	#75原本是90，目的是校正

# Custom angle to set Servo motor angle
def setServoAngle(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.025)

# 初始化並設定初始角度
board.digital[pinBottom].mode = SERVO
setServoAngle(pinBottom, bAngle)
board.digital[pinLeft].mode = SERVO
setServoAngle(pinLeft, lAngle)
board.digital[pinRight].mode = SERVO
setServoAngle(pinRight, rAngle)
board.digital[pinHand].mode = SERVO
setServoAngle(pinHand, hAngle)

curBtmAngel,curLftAngle,curRhtAngle,curHndAngle = bAngle,lAngle,rAngle,hAngle

print('夾兩次:')
print('右轉,curBtmAngel=',curBtmAngel)
angle = 45
for i in range(angle):
    setServoAngle(pinBottom, curBtmAngel-i)
curBtmAngel = curBtmAngel - angle
sleep(0.5)

print('下,curBtmAngel=',curBtmAngel)
angle = 40
for i in range(angle):
    setServoAngle(pinLeft, curLftAngle-i)
curLftAngle = curLftAngle - angle
sleep(0.5)

for s in range(3):

    print('去,curLftAngle=',curLftAngle)
    angle = 40
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle+i)
    curRhtAngle = curRhtAngle + angle
    sleep(0.5)
    print('夾,curRhtAngle=',curRhtAngle)
    angle = 45
    for i in range(angle):
        setServoAngle(pinHand, curHndAngle+i)
    curHndAngle = curHndAngle + angle
    sleep(0.5)
    print('上,curHndAngle=',curHndAngle)
    angle = 40
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle+i)
    curLftAngle = curLftAngle + angle
    sleep(0.5)
    print('回,curLftAngle=',curLftAngle)
    angle = 40
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle-i)
    curRhtAngle = curRhtAngle - angle
    sleep(0.5)
    print('大左轉,curRhtAngle=',curRhtAngle)
    angle = 90
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel+i)
    curBtmAngel = curBtmAngel + angle
    sleep(0.5)
    print('去,curBtmAngel=',curBtmAngel)
    angle = 40 - 4 #回拉
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle+i)
    curRhtAngle = curRhtAngle + angle
    sleep(0.5)
    print('下,curRhtAngle=',curRhtAngle)
    angle = 40
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle-i)
    curLftAngle = curLftAngle - angle
    sleep(0.5)
    print('開,curLftAngle=',curLftAngle)
    angle = 45
    for i in range(angle):
        setServoAngle(pinHand, curHndAngle-i)
    curHndAngle = curHndAngle - angle
    sleep(0.5)
    print('回,curHndAngle=',curHndAngle)
    angle = 40 - 4 #回正
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle-i)
    curRhtAngle = curRhtAngle - angle
    sleep(0.5)
    print('去,curLftAngle=',curLftAngle)
    angle = 40
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle+i)
    curRhtAngle = curRhtAngle + angle
    sleep(0.5)
    print('夾,curRhtAngle=',curRhtAngle)
    angle = 45
    for i in range(angle):
        setServoAngle(pinHand, curHndAngle+i)
    curHndAngle = curHndAngle + angle
    sleep(0.5)
    print('上,curHndAngle=',curHndAngle)
    angle = 40
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle+i)
    curLftAngle = curLftAngle + angle
    sleep(0.5)
    print('回,curLftAngle=',curLftAngle)
    angle = 40
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle-i)
    curRhtAngle = curRhtAngle - angle
    sleep(0.5)
    print('大右轉,curRhtAngle=',curRhtAngle)
    angle = 90
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel-i)
    curBtmAngel = curBtmAngel - angle
    sleep(0.5)
    print('去,curBtmAngel=',curBtmAngel)
    angle = 40 - 4 # 回拉
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle+i)
    curRhtAngle = curRhtAngle + angle
    sleep(0.5)
    print('下,curRhtAngle=',curRhtAngle)
    angle = 40
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle-i)
    curLftAngle = curLftAngle - angle
    sleep(0.5)
    print('開,curLftAngle=',curLftAngle)
    angle = 45
    for i in range(angle):
        setServoAngle(pinHand, curHndAngle-i)
    curHndAngle = curHndAngle - angle
    sleep(0.5)
    print('回,curHndAngle=',curHndAngle)
    angle = 40 - 4 # 回正
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle-i)
    curRhtAngle = curRhtAngle - angle
    sleep(0.5)

print('上,curHndAngle=',curHndAngle)
angle = 40
for i in range(angle):
    setServoAngle(pinLeft, curLftAngle+i)
curLftAngle = curLftAngle + angle
sleep(0.5)

print('左轉,curLftAngle=',curLftAngle)
angle = 45
for i in range(angle):
    setServoAngle(pinBottom, curBtmAngel+i)
curBtmAngel = curBtmAngel + angle
sleep(0.5)
board.exit()

