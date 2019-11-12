import cryptography
import os

from cryptography.fernet import Fernet

input_file = 'text.enc'
output_file = 'text-dec.txt'

with open(input_file, 'rb') as f:
    data = f.read()
with open("key.key", 'rb') as f:
    key = f.read()
fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

os.remove(input_file)