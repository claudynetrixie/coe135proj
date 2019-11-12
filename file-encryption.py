import cryptography

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

file = open('key.key', 'wb')
file.write(key)
file.close()

input_file = 'test.txt'
output_file = 'text.enc'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)


