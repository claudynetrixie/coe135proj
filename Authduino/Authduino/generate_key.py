import cryptography
from cryptography.fernet import Fernet

from os import listdir
from os.path import isfile, join

import os
import itertools
import pwd

user = str(pwd.getpwuid(os.getuid())[0])

#Key Generation
key = Fernet.generate_key()
print(key)
#Key Storage
file = open('/home/' + user + '/Authduino/key.key', 'wb')
file.write(key)
file.close()



#user = str(pwd.getpwuid(os.getuid())[0])
