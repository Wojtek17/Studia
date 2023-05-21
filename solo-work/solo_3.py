class Student:
    def __init__(self, imie_studenta, nazwisko_studenta, nr_indeksu):
        self.imie_studenta = imie_studenta
        self.nazwisko_studenta=nazwisko_studenta 
        self.nr_indeksu=nr_indeksu
        self.indeks=[]
    def __str__(self):
        return self.imie_studenta+' '+self.nazwisko+' '+str(self.nr_indeksu)

    def dodaj_ocene(self,ocena):
        self.indeks.append(ocena)
    def oblicz_srednia(self):
        return sum(self.indeks)/len(self.indeks)
    

student_wojtek=Student("Wojciech","Marszałek",120807)
student_wojtek.dodaj_ocene(4.0)
student_wojtek.dodaj_ocene(3.0)
student_wojtek.dodaj_ocene(5.0)
print(student_wojtek.oblicz_srednia())

class Auto:
    def __init__(self, marka, moc_silnika, kolor, cena, waga, rok_produkcji, przebieg, ma_klimatyzacje):
        self.marka=marka
        self.moc_silnika=moc_silnika
        self.kolor=kolor
        self.cena=cena
        self.waga=waga
        self.rok_produkcji=rok_produkcji
        self.przebieg=przebieg
        self.ma_klimatyzacje=ma_klimatyzacje

    def __str__(self):
        return self.marka+' '+str(self.przebieg)+' '+str(self.rok_produkcji)+' '+str(self.cena)
    
czarny_golf=Auto("Volkswagen", 1.495, "czarny", 50000, 2000, 2016, 25000, True)
print(czarny_golf)