n = int(input())
a = 1
b = 0
while a<= n:
    a *= 2
    b += 1
    if a == n:
        print('YES')
        break
else:
    print('NO')