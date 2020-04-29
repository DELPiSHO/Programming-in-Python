num1 = int(input())
num2 = int(input())

if num1 > num2:
    for i in range(num2,num1):
        if (i % 2 == 0) and (i % 7 == 1):
            print(i)
if num2 > num1:
    for i in range(num1,num2):
        if (i % 2 == 0) and (i % 7 == 1):
            print(i)