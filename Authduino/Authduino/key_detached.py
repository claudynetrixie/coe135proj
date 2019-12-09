import subprocess
import os
import pwd

#generation of new password and hash and storing new pw
#cmd1 = subprocess.Popen(["python", "upload_sketch.py"])


#call encryption here
print("Encrypting here.")
user = str(pwd.getpwuid(os.getuid())[0])
cmd2 = subprocess.Popen(["python", "/home/" + user + "/Authduino/file-encryption.py"])
