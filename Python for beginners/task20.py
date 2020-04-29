h = False
while h == False:
    str = input()
    if 'qwerty' in str:
        print("Слабый пароль")
    elif '1234' in str:
        print("Слабый пароль")
    elif len(str) < 8:
        print("Короткий пароль")
    elif str.isalpha():
        print("Пароль должен содержать цифры")
    else:
        h = True