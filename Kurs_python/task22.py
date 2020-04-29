from sys import argv as args
s = ''
for i in range(1,len(args)):
    s += args[i] + ' '
print(s,end=' ')