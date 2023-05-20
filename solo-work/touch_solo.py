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

#Zadanie 1.7
# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()
for student in studenci:
    print(student)

#Zadanie 1.8
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key=lambda x: x.split()[-1])
for student in studenci:
    print(student)

#Zadanie 1.9
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

first_letter_list=[]
for student in studenci:
    first_letter=student[student.find(" ")+1]
    first_letter_list.append(first_letter)
n_num=first_letter_list.count("N")
print("Liczba studentow na N wynosi: ",n_num)

#Zadanie 1.10
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

wykres_1_funkcja_liniowa = True
wykres_2_funkcja_liniowa = True
wykres_3_funkcja_liniowa = False

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")