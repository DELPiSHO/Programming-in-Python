n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(1, n + 1):
        print(b, end=' ')
        a, b = b, a + b