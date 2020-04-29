num1 = int(input())
num2 = int(input())
sum = 0
if num1 > num2:
    for i in range(num2,num1):
        sum += i ** 2
elif num2 > num1:
    for i in range(num1,num2):
        sum += i ** 2
print(sum)