#similar to task77
a = [i for i in iter(input, '.')]
b = [int(input()) - 1 for i in range(int(input()))]
for i in b:
    print(a[i], end='')