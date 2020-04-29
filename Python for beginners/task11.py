num1 = int(input())
num2 = int(input())
num = max(num1,num2) - min(num1,num2)
hours = num // 60
minutes = num % 60
print(hours, minutes)