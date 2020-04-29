s = []
sum = 0
sqSum = 0

while(True):
    a = int(input())
    sum += a
    if(sum == 0):
        s.append(a)
        break
    s.append(a)

for i in range(len(s)):
    sqSum += int(s[i]) ** 2
print(sqSum)
