#Wybranie poziomu trudności od 2 do 10

poziomTrudnosci = int(input("Podaj poziom trudności od 2 do 10: "))
if (poziomTrudnosci < 2 or poziomTrudnosci > 10):
    print("Podałeś złą wartość. Jeszcze raz")

ileSzans = int(input("Podaj liczbę prób: "))


#Wygenerowanie magic number
from random import randrange
magicNumber = randrange(poziomTrudnosci)
print(magicNumber)

#Poproszenie użytkownika o strzał

for i in range(ileSzans):
    strzal = int(input("Strzelaj! "))
    if (strzal == magicNumber):
        print("GRATULACJE!!! WYGRAŁEŚ!!!")
        break
    elif (strzal < magicNumber):
        print("Dałeś trochę za mało...")
    else:
        print("Dałeś trochę za dużo...")
