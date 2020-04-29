num1 = int(input())
num2 = int(input())
if (num1 > num2):
    print(tuple(range(num2,num1)))
elif (num2 > num1):
    print(tuple(range(num1, num2)))
