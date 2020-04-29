import re
password = input()
if 'qwerty' in password:
    print("Bad password")
elif '1234' in password:
    print("Bad password")
elif password.isalpha() == True:
    print("Bad password")
elif len(password) < 8:
    print("Bad password")
else:
    print("Good password")