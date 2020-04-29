re4 = []
c = '3'
new = []
while c != '.':
    c = input()
    re4.append(c)
print(re4)
n = int(input())
for i in range(n):
    b = int(input())
    new.append(re4.index(b))
print(new)