a = int(input())
b = int(input())
list = []
for i in range(b+1,a+1):
    list.append(i)
list.reverse()
for i in list:
    print(i)