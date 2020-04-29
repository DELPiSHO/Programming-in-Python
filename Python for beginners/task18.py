num1 = float(input())
num2 = float(input())
sign = input()

if sign == '/' and num2 != 0:
    print(num1/num2)
elif sign == '*' and num2 != 0:
    print(num1*num2)
elif sign == '-':
    print(num1-num2)
elif sign == '+':
    print(num1+num2)