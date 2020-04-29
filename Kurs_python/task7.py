a = input().split()
a.sort()
for i in set(a):
    if (a.count(i) <= 1):
        continue
    else:
        print(i)