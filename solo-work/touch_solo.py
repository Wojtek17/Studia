#Zadanie 1.1
hello="Hello"
name="Wojtek"
print(hello,name)

#Zadanie 1.2
name=input("Wpisz imie")
print("Hello ",name)

#Zadanie 1.3
studenci = ["Ania", "Kuba", "Piotr", "Jan"]
liczba_studentow=len(studenci)
print("Liczba studentow wynosi: ",liczba_studentow)

#Zadanie 1.4
studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
for student in studenci:
    print("Hello ",student)

#Zadanie 1.5

liczba = 5
potega = 7
wynik=liczba**potega

print("Wynik wynosi: ",wynik)

#Zadanie 1.6
ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))