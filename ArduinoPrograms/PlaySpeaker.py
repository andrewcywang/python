from pyfirmata import Arduino
from time import sleep

# 定義八個燈號的 port
led1, led2, led3, led4, led5, led6, led7, led8, speaker = 2, 3, 4, 5, 6, 7, 8, 9, 10
# 定義八個音
notes = [ 261, 294, 330, 349, 392, 440, 494, 523 ]
delay_sec = [ 500/x/1000 for x in notes ]
print(delay_sec)

port = 'COM3'
board = Arduino(port)

for i in range(100):
    board.digital[speaker].write(1)
    sleep(0.001)
    board.digital[speaker].write(0)
    sleep(0.001)

sleep(0.2)
print('Play Do', delay_sec[0])

for i in range(100):
    board.digital[speaker].write(1)
    sleep(0.003)
    board.digital[speaker].write(0)
    sleep(0.003)

sleep(0.2)
print('Play Re', delay_sec[1])

tempo = 400




