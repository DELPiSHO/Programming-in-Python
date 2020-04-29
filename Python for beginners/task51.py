numbers = tuple(map(int, input().split()))
maxx = []
new = []
if len(numbers) == 0:
    print('Не найдено')
    exit()
for i in range(len(numbers)):
    if numbers[i] > 9 and numbers[i] < 100:
        maxx.append(numbers[i])
    else:
        continue
for i in maxx:
    if i % 3 != 0:
        new.append(i)
    else:
        continue
if not new:
    print('Не найдено')
else:
    high = new[0]
    for i in new:
        if i > int(high):
            high = i
        else:
            continue
    print(high)
