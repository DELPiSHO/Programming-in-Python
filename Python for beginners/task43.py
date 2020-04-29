num = int(input())
i = 0
j = 1
while j <= num:
    str = input()
    if 'rat' in str:
        i += 1
        print(j)
        break
    j += 1
if i == 0:
    print(-1)