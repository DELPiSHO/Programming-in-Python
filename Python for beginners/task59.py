c = '3'
error = "@@"
warning = "!!"
info = "//"
verbose = "**"
while c != '.':
    c = input()
    if error in c:
        print("ошибка")
    elif warning in c:
        print("предупреждение")
    elif info in c:
        print("информация")
    elif verbose in c:
        print("подробное сообщение")
    else:
        continue
