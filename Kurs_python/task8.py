a = input().split()
sum = []
for i in range(0,len(a)):
    if(len(a) == 1):
        sum.append(int(a[i]))
    elif (i == 0):
        sum.append(int(a[len(a)-1]) + int(a[i+1]))
    elif (i == len(a) -1):
        sum.append(int(a[i-1]) + int(a[0]))
    else:
        sum.append(int(a[i-1]) + int(a[i+1]))
for j in sum:
    print(j, end=' ')

