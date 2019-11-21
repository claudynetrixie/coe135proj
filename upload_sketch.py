import os
import random, string
import bcrypt

password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
print(password)


#print("Password generated:  " + generate_password(50))

with open("test.ino", "r") as file:
    data = file.readlines()

data[4] = "  Serial.println(\"" + password + "\");\n"

with open('test.ino', 'w') as file:
    file.writelines( data )

#this generates the hashed password to be stored
salt = bcrypt.gensalt()
password_hashed = bcrypt.hashpw(password, salt)

print("Hashed:  " + password_hashed)

cmd = 'arduino --upload [test.ino]'
os.system(cmd)
