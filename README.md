# ESET - Challenge 9 - JS Reverser

As this challenge is about reversing the JS Code in order to solve how actually the backend code is calculating the password.

So, we will be writing the python script in order to automate the process.

## 1. Taking User Input
The first and the foremost thing is to fetch the user input. We can use system arguments and we can use input function. Let's keep it basic and go with the input function.

```
import sys

password = input("Enter Password: ")
```

Once we have taken the user input. The next thing is to check it's length. Whether it is less than 10 or greater than 20. 

```
if len(password) < 10 or len (password) > 20:
		print("Password can not be accepted")
		sys.exit()
```

So, we will calculate the length of password in **IF** condition. If the password is of desired length. We will move onto calculating its ordinal value i.e. the corresponding ASCII table value for each user input.

```
else:
		index = 1
		for val in password:
		index += ord(val)
		print(val)
```

Once we have calculated all the ordinal values and their sum. We need to find the modulus. Thus,

```
modulus = index%421
```

Now, we need to calculate whether the modulus value was equal to 0 or not. If it was equal we have generated the correct password. If not, we got to try again.

```
if modulus == 0:
		print("Correct Password: " + password)
else:
		print("Wrong Password!")
```

