c = '3'
slov = []
new = []
while c != '.':
    c = input()
    if c == '.':
        break
    else:
        slov.append(c)
for i in slov:
    a = ' '.join(i.upper())
    print(a)