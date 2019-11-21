import bcrypt

password = "gZc0XaHNpt3R40BN"
salt = bcrypt.gensalt()
password_hashed = bcrypt.hashpw(password, salt)
password_hashed = "$2a$12$/L.nM21wY05.wVeZSZyIZeI5BYbq5nz9/gzExx6KiNnkja4H93HeS"
# store 'password_hashed' in a database of your choosing
print("MyPassword: " + password_hashed)

if bcrypt.hashpw(password, password_hashed) == password_hashed:
    print("MATCH\n");
else:
    print("fail")
