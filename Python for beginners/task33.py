money = int(input())
number = int(input())

for i in range(number):
    money -= int(input())

if money >= 0:
    print("Покупает")
else:
    print("Не покупает")