import os
import random, string
import bcrypt
import pwd
import cryptography
from cryptography.fernet import Fernet

user = str(pwd.getpwuid(os.getuid())[0])

#Key Generation
password = Fernet.generate_key()
#Key Storage
file = open('/home/' + user + '/Authduino/key.key', 'wb')
file.write(password)
file.close()

#upload new password to key
with open("/home/" + user + "/Authduino/test/newcrypt.ino", "r") as file:
    data = file.readlines()

data[4] = "  Serial.println(\"" + password + "\");\n"
print(data)

with open('/home/' + user + '/Authduino/test/newcrypt.ino', 'w') as file:
    file.writelines(data)



cmd = 'arduino --upload /home/'+ user + '/Authduino/test/newcrypt.ino'
os.system(cmd)

print("done")
