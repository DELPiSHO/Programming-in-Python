numbers = tuple(map(int, input().split(',')))
ind = 0
suma = 0
minn = min(numbers)
for i in range(len(numbers)):
    if numbers[i] == minn:
        suma += i
print(suma)