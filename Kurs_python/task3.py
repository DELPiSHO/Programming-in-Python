a = int(input())
b = int(input())
sr = 0
len = 0
for i in range (a,b+1):
    if(i % 3 == 0):
        sr += i
        len += 1
    else:
        continue
print(sr/len)
