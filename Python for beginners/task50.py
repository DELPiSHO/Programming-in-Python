numbers = tuple(map(int, input().split()))
r = 0
suma = 0
n = 0

for i in range(len(numbers)-1):
    if i == len(numbers):
        break
    n = numbers[i] + numbers[i+1]
    if n % 3 == 0 and n % 9 != 0:
        print(n)
        suma += 1
        n = 0
    else:
        n = 0
print(suma)