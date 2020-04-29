c = '3'
lista = []
while c != '.':
    c = input()
    if c == '.':
        break
    else:
        lista.append(c)
if len(lista) % 2 != 0:
    print(lista[len(lista) // 2])
else:
    a = len(lista) // 2 - 1
    b = len(lista) // 2
    i = ((int(lista[a]) + int(lista[b]))/2)
    print(i)