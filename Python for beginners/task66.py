def getchar(string, n):
    return str(string)[n - 1]

a = " python "
c = '3'
k = 0
n = 0
list = []
new = []

while c != '.':
    c = input()
    if c == '.':
        break
    elif c.find('python') == True:
        k += 1
        list.append(c)
    else:
        list.append(c)

for i in list:
    new.append(getchar(i,k))

new = ' '.join(new)
print(new)