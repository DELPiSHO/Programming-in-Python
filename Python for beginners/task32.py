num1 = int(input())
list = ('Красный','Оранжевый','Желтый','Зеленый','Голубой','Синий','Фиолетовый')
if num1 > 7:
    print("Радуга состоит только из семи цветов")
elif num1 > 0 and num1 <= 7:
    for i in range(num1):
        print(list[i])
