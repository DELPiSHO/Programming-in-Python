num = int(input())
a = []
i = 0
while (len(a) < num):
    a += [i] * i
    i += 1
print(*a[:num])