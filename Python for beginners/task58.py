c = '3'
lista = []
new = []
while c != '.':
    c = input()
    if c == '.':
        break
    else:
        lista.append(c)
lista.reverse()
for i in lista:
    i = int(i) * int(i)
    new.append(i)
new = ' '.join(str(i) for i in new)
print(new)
