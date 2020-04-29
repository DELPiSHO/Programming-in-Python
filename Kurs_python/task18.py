d = {}
for _ in range(int(input())):
    x = int(input())
    if x not in d:
        d[x] = f(x)
    print(d[x])