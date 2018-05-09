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
bAngle, lAngle, rAngle, hAngle = 75, 90, 90, 0	#75是為了校正左右角度，原本應該是90

# Custom angle to set Servo motor angle
def setServoAngle(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

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
print('搖頭一次:')	#讓系統顯示執行狀態
for s in range(1):
    angle = 60
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel-i)
    curBtmAngel = curBtmAngel - angle
    angle = 120
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel+i)
    curBtmAngel = curBtmAngel + angle
    angle = 60
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel-i)
    curBtmAngel = curBtmAngel - angle
print('底盤角度',curBtmAngel)

print('抬頭三次:')
for s in range(3):
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle+i)
    curLftAngle = curLftAngle + angle
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle-i)
    curLftAngle = curLftAngle - angle
print('高低角度',curLftAngle)

print('前後兩次:')
for s in range(2):
    angle = 60
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle-i)
    curRhtAngle = curRhtAngle - angle
    angle = 120
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle+i)
    curRhtAngle = curRhtAngle + angle
    angle = 60
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle-i)
    curRhtAngle = curRhtAngle - angle
print('前後角度',curRhtAngle)

print('磕頭兩次:')
angle = 60
for s in range(2):
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle-i)
        setServoAngle(pinRight, curRhtAngle+i)
    curLftAngle = curLftAngle - angle
    curRhtAngle = curRhtAngle + angle
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle+i)
        setServoAngle(pinRight, curRhtAngle-i)
    curLftAngle = curLftAngle + angle
    curRhtAngle = curRhtAngle - angle
print('磕頭角度',curLftAngle,curRhtAngle)

print('夾三次:')
for s in range(3):
    # 右轉
    angle = 60
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel-i)
    curBtmAngel = curBtmAngel - angle
    # 下
    angle = 42
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle-i)
    curLftAngle = curLftAngle - angle
    # 去
    angle = 42
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle+i)
    curRhtAngle = curRhtAngle + angle
    # 夾
    angle = 45
    for i in range(angle):
        setServoAngle(pinHand, curHndAngle+i)
    curHndAngle = curHndAngle + angle
    # 上
    angle = 42
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle+i)
    curLftAngle = curLftAngle + angle
    # 回
    angle = 42
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle-i)
    curRhtAngle = curRhtAngle - angle
    # 左轉120
    angle = 120
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel+i)
    curBtmAngel = curBtmAngel + angle
    # 去
    angle = 42
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle+i)
    curRhtAngle = curRhtAngle + angle
    # 下
    angle = 42
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle-i)
    curLftAngle = curLftAngle - angle
    # 開
    angle = 45
    for i in range(angle):
        setServoAngle(pinHand, curHndAngle-i)
    curHndAngle = curHndAngle - angle
    # 回
    angle = 42
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle-i)
    curRhtAngle = curRhtAngle - angle
    # 上
    angle = 42
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle+i)
    curLftAngle = curLftAngle + angle
    # 右轉
    angle = 60
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel-i)
    curBtmAngel = curBtmAngel - angle

    # 反向開始:左轉
    angle = 60
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel+i)
    curBtmAngel = curBtmAngel + angle
    # 下
    angle = 42
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle-i)
    curLftAngle = curLftAngle - angle
    # 去
    angle = 42
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle+i)
    curRhtAngle = curRhtAngle + angle
    # 夾
    angle = 45
    for i in range(angle):
        setServoAngle(pinHand, curHndAngle+i)
    curHndAngle = curHndAngle + angle
    # 上
    angle = 42
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle+i)
    curLftAngle = curLftAngle + angle
    # 回
    angle = 42
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle-i)
    curRhtAngle = curRhtAngle - angle
    # 右轉120
    angle = 120
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel-i)
    curBtmAngel = curBtmAngel - angle
    # 去
    angle = 42
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle+i)
    curRhtAngle = curRhtAngle + angle
    # 下
    angle = 42
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle-i)
    curLftAngle = curLftAngle - angle
    # 開
    angle = 45
    for i in range(angle):
        setServoAngle(pinHand, curHndAngle-i)
    curHndAngle = curHndAngle - angle
    # 回
    angle = 42
    for i in range(angle):
        setServoAngle(pinRight, curRhtAngle-i)
    curRhtAngle = curRhtAngle - angle
        # 上
    angle = 42
    for i in range(angle):
        setServoAngle(pinLeft, curLftAngle+i)
    curLftAngle = curLftAngle + angle
    # 左轉
    angle = 60
    for i in range(angle):
        setServoAngle(pinBottom, curBtmAngel+i)
    curBtmAngel = curBtmAngel + angle
board.exit()

