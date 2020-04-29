numbers = input().split()
first = []
second = []
suma = 0
if len(numbers) % 2 == 0:
    for i in range(len(numbers) // 2):
        first.append(int(numbers[i]))
    for i in range(len(numbers) // 2,len(numbers)):
        second.append(int(numbers[i]))
else:
    for i in range(len(numbers) // 2):
        first.append(int(numbers[i]))
    for i in range(len(numbers) // 2 ,len(numbers)):
        second.append(int(numbers[i]))
first.sort()
second.sort(reverse = True)
firstel,secondel = first[0],second[-1]
suma = int(firstel) + int(secondel)
print(suma)