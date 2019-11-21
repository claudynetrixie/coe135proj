import cryptography

from cryptography.fernet import Fernet

from os import listdir
from os.path import isfile, join

import os
import itertools

mypath = "/home/claudyne/Desktop/encrypted"

#Getting Input Files
input_files = [f for f in listdir(mypath) if isfile (join(mypath,f))]
num_file = len(input_files)

output_files = []
input_paths = []
output_paths = []

for i in input_files:
	output_files.append((str(os.path.splitext(i)[0])) + '.enc')
	input_paths.append(mypath +"/" +i)

for i in output_files:
	output_paths.append(mypath + "/" + i)

#Key Generation
key = Fernet.generate_key()
print(key)
#Key Storage
file = open('key.key', 'wb')
file.write(key)
file.close()

data = []
encrypted = []

for i in input_paths:
	with open(i, 'rb') as f:
	    data.append(f.read())

fernet = Fernet(key)

for i in data:
	encrypted.append(fernet.encrypt(i))


for (i,x) in zip(output_paths, encrypted):
	with open(i, 'wb') as f:
	    f.write(x)

for i in input_paths:
	os.remove(i)

