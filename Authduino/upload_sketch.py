import os
import random, string
import bcrypt
import pwd

#generates random password
#edit if you want to change way of generating random password
password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
print(password)

user = str(pwd.getpwuid(os.getuid())[0])

#upload new password to key
with open("/home/" + user + "/Authduino/test/test.ino", "r") as file:
    data = file.readlines()

data[4] = "  Serial.println(\"" + password + "\");\n"

with open('/home/' + user + '/Authduino/test/test.ino', 'w') as file:
    file.writelines( data )

#this generates the hashed password to be stored
salt = bcrypt.gensalt()
password_hashed = bcrypt.hashpw(password, salt)

#stores hashed password
f = open("/home/" + user + "/Authduino/config.info","w+")
f.write(password_hashed)
f.close()
print("Hashed:  " + password_hashed)

cmd = 'arduino --upload test/test.ino'
os.system(cmd)

print("done")
