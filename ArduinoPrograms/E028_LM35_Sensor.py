import serial
"""download library file from
https://pypi.python.org/pypi/pyserial """
temp='0';
ser = serial.Serial(port='COM4',baudrate=9600)
               #enter comport name,baud rate
ser.close()              #closes previously open serial port
ser.open()                   # opens serial port
x = ser.read()#reads a byte of the data .
while x == chr(0x0d):
    x = ser.read()
while True:
    x = ser.read()#reads a byte of the data .
    if x == chr(0x0d):
        x = ser.read()
        print('temperature is', temp, ' \n')
        temp='0';
    else:
        temp = temp + x
