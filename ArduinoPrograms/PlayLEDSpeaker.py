import pyfirmata
from time import sleep
# 定義八個燈號的 port
led1, led2, led3, led4, led5, led6, led7, led8= 2, 3, 4, 5, 6, 7, 8, 9
# 定義八個音
notes = [ 261, 294, 330, 349, 392, 440, 494, 523 ]
port = 'COM3'
board = pyfirmata.Arduino(port)

def style():
    for i in range(led1, led8 + 1):
        board.digital[i].write(1)
        sleep(0.2)
    for i in range(led8, led1 - 1, -1):
        board.digital[i].write(0)
        sleep(0.2)

for i in range(1):
    style()

def play_note(x):
    global last
    for i in x:
        board.digital[i].write(1)
        board.tone(10,tones[i]-1,400)
        sleep(0.4)
        board.digital[i].write(0)        
        board.noTone(10)
        
play = [led5, led3, led3, led4, led2, led2]

play_note(play)




