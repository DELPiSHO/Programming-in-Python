num1 = int(input())
num2 = int(input())
suma = 0
if num1 > num2:
    for i in range(num2,num1):
        suma += i
elif num2 > num1:
    for i in range(num1,num2):
        suma += i
print(suma)