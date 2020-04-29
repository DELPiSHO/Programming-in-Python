import datetime

class Osoba():
    def __init__(self, slownik):
        self.w =[] #slownik kluczy
        self.slownik=slownik #potrzebny do wypisywania
        for key in slownik:
            setattr(self, key, slownik[key]) #tworzenie odiektu Osoba ze slownika
            self.w.append(str(key))          #przypisywanie kluczy do slownika
        self.bmi = self.znajdzBMI()


    def znajdzBMI(self):                   #metoda liczaca BMI
        x = (float(self.wzrost)) / 100  # wyliczamy bmi formula: waga/(wzrost/100)^2
        self.bmi = (self.waga / (x * x))
        return str(self.bmi)[:5]    #ograniczenie 2 cyfry po przecinku


    def __str__(self):          #wypisywanie
        druk = ""
        for x in range(len(self.w)):
            druk += str(self.w[x]).capitalize() + ": " + str(self.slownik[self.w[x]]).capitalize() + "\n"
        return str(druk) + "bmi: " + self.bmi + "\n"
        
class Osoby(Osoba):
    
    def __init__(self,krotka):
        self.lista=[]       #tworzymy pusta liste do osob
        for x in range (0,len(krotka)):
            self.lista.append(Osoba(krotka[x]))
            
    def __str__(self):
        druk=''
        i = 0
        sort = sorted(self.lista)   #sortowanie listy z osobami

#        for x in range(0,len(self.lista)):
#           druk +=(self.lista[x]) + "\n"
