import serial
import time
from os.path import expanduser
import datetime
import bcrypt
import os

arduino = serial.Serial("/dev/ttyUSB0", 9600, timeout = 5, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, xonxoff = 0, rtscts = 0);


time.sleep(2)
data = arduino.readline()
time.sleep(2)

print (data)

file = open(expanduser("~") + '/Desktop/script.log', 'a')
file.write("Encrypted Key: " + data + " " + str(datetime.datetime.now()) + " " + str(os.getpid()) + "\n")
file.close()

data = data.rstrip()
hashed = "$2a$12$/L.nM21wY05.wVeZSZyIZeI5BYbq5nz9/gzExx6KiNnkja4H93HeS"
#data = "gZc0XaHNpt3R40BN"
print("[" + data + "]")
if bcrypt.hashpw(data, hashed) == hashed:
    print("MATCH\n");
else:
    print("fail")
