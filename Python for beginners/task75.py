n = input()
lista = []
new = []
numbers = []
for i in n:
    if i.isdigit():
        i = int(i) + 1
        lista.append(i)
    else:
        lista.append(i)
for i in lista:
    if i == 10:
        i = 0
        new.append(i)
    else:
        new.append(i)
new = ''.join(str(i) for i in new)
print(new)