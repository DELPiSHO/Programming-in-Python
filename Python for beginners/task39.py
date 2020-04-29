num = int(input())

for i in range(1,num + 1):
    for j in range(1,num + 1):
        if j == num:
            print(i*j,end='\n')
        else:
            print(i*j,end='\t')