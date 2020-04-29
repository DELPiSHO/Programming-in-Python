opinions = int(input())
city = input()
language = input()

if (opinions >= 7) and (city == 'Рим') and (('английский' in language) or ('русский' in language)):
    print("Подходит")
else:
    print('Не подходит')