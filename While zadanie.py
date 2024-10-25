#Program ktory dodaje liczby podane przez uzytkownika

#Inicjalizacja programu
print("Witaj w dodawaniu liczb!")

#Pobranie od usera informacji ile liczb chce dodac
ilosc = int(input("Ile liczb bedziesz dodawac? "))

#Definicja sumy, poczatkowa wartosc ustawiona na zero
suma = 0

#Glowna sekcja while
i = 0

while i < ilosc:
    x = int(input("Podaj liczbe ktora chcesz dodac: "))
    suma += x
    i += 1
print("Wynik to: ", suma)
