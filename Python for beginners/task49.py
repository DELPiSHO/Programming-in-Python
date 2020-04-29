sum = 0
num = int(input())
for i in range(num):
    n = int(input())
    if n % 6 == 0:
        sum += n
    else:
        continue
print(sum)