n = int(input())
inp = []
for i in range(n):
    inp.append(int(input()))

minc = inp[0]
minn = inp[0]

for i in range(n):
    if inp[i] % 2 == 0 and inp[i] < minc:
        minc = inp[i]
    if inp[i] % 2 != 0 and inp[i] < minn:
        minn = inp[i]
m = minn + minc

for i in range(n):
    if inp[i] <= m:
        g = inp[i] + m
        print(g, end=' ')
    else:
        so = inp[i]
        print(so, end=' ')