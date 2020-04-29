from math import *

def czynnikiPierwsze(liczba):
    if liczba <= 0:
        return 0
    i = 2
    lista = []
    pomocnicza = floor(sqrt(liczba))
    while i <= pomocnicza:
        if liczba % i == 0:
            lista.append(i)
            liczba /= i
            pomocnicza = floor(sqrt(liczba))
        else:
            i += 1
    if liczba > 1:
        lista.append(liczba)
    return lista

def liczbaIWykladnik(lista):
    pierwsza=lista[0]
    x=1
    licznik=1
    nowa=[]
    while x < len(lista):
        if pierwsza == lista[x]:
            licznik+=1
        else: break
        x+=1
    if licznik == len(lista):
        nowa.append(pierwsza)
        nowa.append(licznik)
        return nowa
    else: return 0

#sprawdzenie czynnikiPierwsze
#print("Podaj liczbę: ")
#l = int(input())
#lista = czynnikiPierwsze(l)
#print(lista)

#sprawLiczbaWykladnik
#nowa = liczbaIWykladnik(lista)
#nowa = liczbaIWykladnik(czynnikiPierwsze(l))
#print(nowa)


