from ludzie import *

krotka = (
{'nazwisko': 'Beacka','imie': 'Anna', 'wzrost': 160, 'waga': 65},
{'nazwisko': 'Cezarski', 'imie':'Cezary', 'wzrost': 180, 'waga': 75},
{'nazwisko': 'Darecki', 'imie': 'Dariusz', 'wzrost': 185, 'waga': 85},
{'imie': 'Anna', 'nazwisko': 'Annecka', 'wzrost': 170, 'waga': 60},
{'imie': 'Dariusz', 'nazwisko': 'Francki', 'wzrost': 179, 'waga': 85},
{'imie': 'Henryk', 'nazwisko':'Cerski','waga': 85, 'wzrost': 189}
)

test=Osoba(krotka[0])
print(test.bmi)

#osoby = Osoby(krotka)

#print(osoby.lista)