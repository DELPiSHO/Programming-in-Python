num = input().split()
first = int(num[0])
second = int(num[1])
new = []
for i in range(first,second + 1):
    new.append(i ** int(num[-1]))
print(*new)