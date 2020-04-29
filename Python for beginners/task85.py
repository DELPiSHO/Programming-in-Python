def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num1 = int(input())
num2 = int(input())
suma = 0
for i in range(num1,num2+1):
    suma += factorial(i)
print(suma)