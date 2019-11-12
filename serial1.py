import serial
import time

arduino = serial.Serial("/dev/ttyUSB0", 9600, timeout = 5, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, xonxoff = 0, rtscts = 0);


time.sleep(2)
data = arduino.readline()
time.sleep(1)

print (data)





