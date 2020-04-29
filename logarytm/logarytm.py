import math
from funkcje import *

class ZlaPodstawa(Exception):
    def __str__(self):
        return "Zła podstawa"
class ZlyArgument(Exception):
    def __str__(self):
        return "Zly argument"
class RoznePodstawy(Exception):
    def __str__(self):
        return "Rozne Podstawy"

class Logarytm:
    def __init__(self ,podstawa ,argument):
        if podstawa == 1 or podstawa <= 0:
            raise ZlaPodstawa()
        self.podstawa= podstawa
        if argument <= 0:
            raise ZlyArgument()
        self.argument= argument
    def __add__(self ,other):
        if other.podstawa!=self.podstawa:
            raise RoznePodstawy()
        return Logarytm(self.podstawa ,(other.argument *self.argument))
    def redukuj(self):
        a = liczbaIWykladnik(czynnikiPierwsze(self.podstawa))
        self.podstawa = a[0]
        self.argument = pow(self.argument,1/a[1])
    def oblicz(self):
        wynik = math.log(self.argument ,self.podstawa)
        return int(wynik)
    def __str__(self):
            return "log " +str(self.podstawa ) +"( " +str(self.argument ) +")"


try:

    l1 =Logarytm(8 ,27)
    l2 =Logarytm(2 ,4)
    #l3=Logarytm(1,5)         #Zla podstawa
    # l4=Logarytm(10,0)       #Zly argument
    l1.redukuj()
    print(l1)


except ZlaPodstawa as zp:
    print(zp)
except ZlyArgument as za:
    print(za)

try:
    print(l1 +l2)
except RoznePodstawy as rp:
    print(rp)

l2.oblicz()
print(math.log(4,2))
