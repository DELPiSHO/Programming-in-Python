numbers = tuple(map(float, input().split()))
maxx = 0

for i in range(len(numbers)-1):
    n = abs(numbers[i] - numbers[i+1])
    if n > maxx:
        maxx = n
        num1 = numbers[i]
        num2 = numbers[i+1]
print(num1,end=' ')
print(num2)