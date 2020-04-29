def calc(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return(d * d > n)
a = int(input())
s = 0
for g in range(2,a+1):
    if calc(g) == True:
        s += 1
print(s)