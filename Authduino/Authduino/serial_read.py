import serial
import time
from os.path import expanduser
import datetime
import bcrypt
import os
from os import listdir
from os.path import isfile, join
import cryptography
from cryptography.fernet import Fernet
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
f = open("/home/" + user + "/Authduino/key.key", "r")
hashed = f.read()

if bcrypt.hashpw(data, hashed) == hashed:
    #put decryption here
    print("Starting decryption of files.\n")
    user = str(pwd.getpwuid(os.getuid())[0])

    mypath = "/home/" + user + "/AuthduinoDocs"
    #Getting Input Files
    input_files = [f for f in listdir(mypath) if isfile (join(mypath,f))]

    print("input files:\n")
    print(sorted(input_files))

    key = data

    fernet = Fernet(key)

    with open(mypath + "/" + sorted(input_files)[0], 'rb') as f:
        ext_log = f.read()


    enc_ext_log = (fernet.decrypt(ext_log))

    enc_ext_list = enc_ext_log.split("\n")

    del enc_ext_list[-1]

    output_files = []
    input_paths = []
    output_paths = []

    for (i,x) in zip(sorted(input_files), enc_ext_list):
    	output_files.append((str(os.path.splitext(i)[0])) + x)
    	input_paths.append(mypath +"/" +i)
    	print i

    for i in output_files:
    	output_paths.append(mypath + "/" + i)

    print (output_paths)

    data = []
    encrypted = []

    for i in input_paths:
        with open(i, 'rb') as f:
            data.append(f.read())

    for i in data:
        encrypted.append(fernet.decrypt(i))

    for (i,x) in zip(output_paths, encrypted):
        with open(i, 'wb') as f:
            f.write(x)

    for i in input_paths:
        os.remove(i)



    cmd2 = subprocess.Popen(["python", "/home/" + user + "/Authduino/upload_sketch.py"])

    print("Password matched\n")
else:
    print("Fail")

#put encryption here
