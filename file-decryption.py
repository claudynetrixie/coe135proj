import cryptography
from cryptography.fernet import Fernet

from os import listdir
from os.path import isfile, join

import os
import itertools
import pwd

print("Starting decryption of files.\n")
user = str(pwd.getpwuid(os.getuid())[0])

mypath = "/home/" + user + "/AuthduinoDocs"
#Getting Input Files
input_files = [f for f in listdir(mypath) if isfile (join(mypath,f))]

print("input files:\n")
print(sorted(input_files))
with open("/home/" + user + "/Authduino/key.key", 'rb') as f:
    key = f.read()

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
