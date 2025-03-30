import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.write(b'Hello UART\n')
ser.close()