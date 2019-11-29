import serial
import time
from os.path import expanduser
import datetime
import bcrypt
import os
import subprocess
import pwd

arduino = serial.Serial("/dev/ttyUSB0", 9600, timeout = 5, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, xonxoff = 0, rtscts = 0);


time.sleep(2)
data = arduino.readline()
time.sleep(2)

print (data)
user = str(pwd.getpwuid(os.getuid())[0])
file = open('/home/' + user + '/Authduino/script.log', 'a')
file.write("Encrypted Key: " + data + " " + str(datetime.datetime.now()) + " " + str(os.getpid()) + "\n")
file.close()

data = data.rstrip()

#open config file for checking password_hash
f = open("/home/" + user + "/Authduino/config.info", "r")
hashed = f.read()

if bcrypt.hashpw(data, hashed) == hashed:
    #put decryption here
    cmd1 = subprocess.Popen(["python", "/home/" + user + "/Authduino/file-decryption.py"])
    cmd2 = subprocess.Popen(["python", "/home/" + user + "/Authduino/upload_sketch.py"])

    print("Password matched\n")
else:
    print("Fail")

#put encryption here