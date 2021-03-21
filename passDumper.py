# Author - Kamran Saifullah a.k.a deFr0ggy
# passDumper - Script to solve ESET JS Reversing Challenge
# Date - 21/3/21

import sys

password = input("Enter Password: ")

if len(password) < 10 or len(password) > 20:
    print("Password can not be accepted!")
    sys.exit()
else:
    index = 1
    print("Printing Octal Values!")
    for val in password:
        index += ord(val)
        print(index)

print("\n")
print(index)
modulus = index%421
print("\n")
print(modulus)

if modulus == 0:
    print("Correct Password: " + password)
else:
    print("Wrong Password!")