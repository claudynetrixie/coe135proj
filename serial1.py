import serial
import time
from os.path import expanduser
import datetime
import os

arduino = serial.Serial("/dev/ttyUSB0", 9600, timeout = 5, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, xonxoff = 0, rtscts = 0);


time.sleep(2)
data = arduino.readline()
time.sleep(2)

print (data)

file = open(expanduser("~") + '/Desktop/script.log', 'a')
file.write("Encrypted Key: " + data + " " + str(datetime.datetime.now()) + " " + str(os.getpid()) + "\n")
file.close()



