text = input().split()
skok = int(input())
start = int(input())
lista = []
for i in range(start-1,len(text),skok):
    lista.append(text[i])
lista = ' '.join(lista)
print(lista)
