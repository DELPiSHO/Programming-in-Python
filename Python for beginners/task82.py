numbers = tuple(map(int, input().split(',')))
maxx = 0
helper = max(numbers)
for i in range(len(numbers)):
    if numbers[i] == helper:
        maxx +=1
    else:
        continue
print(maxx)