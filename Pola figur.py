#Start

pi = 3.1415
while(True):
    print()
    print("Witaj w programie 'Pola figur'!")
    print()
    


    #Menu

    print("1. Prostokat")
    print("2. Kwadrat")
    print("3. Trójkat")
    print("4. Trapez")
    print("5. Kolo")

    #Definicje funkcji

    def poleProstokata(a, b):
        return a * b

    def poleKwadratu(a):
        return a ** 2

    def poleTrojkata(a, h):
        return (0.5 * a) * h

    def poleTrapezu(a, b, h):
        return 0.5 * (a + b) * h

    #Pobranie wartosci od uzytkownika

    wybor = input("Wybierz dostepna opcje: ")

    #Glowna sekcja

    if (wybor == "1"):
        a = float(input("Podaj wartosc a: "))
        if (a <= 0):
            print("Podaj prawidlowa wartosc!")
            continue
        b = float(input("Podaj wartosc b: "))
        if (b <= 0):
            print("Podaj prawidlowa wartosc!")
            continue
        print("Pole prostokata wynosi: ", poleProstokata(a, b))
    elif (wybor == "2"):
        a = float(input("Podaj wartosc a: "))
        if (a <= 0):
            print("Podaj prawidlowa wartosc!")
            continue
        else:
            print("Pole kwadratu wynosi: ", poleKwadratu(a))
    elif (wybor == "3"):
        a = float(input("Podaj wartosc podstawy a: "))
        if (a <= 0):
            print("Podaj prawidlowa wartosc!")
            continue
        h = float(input("Podaj wartosc wysokosci h: "))
        if (h <= 0):
            print("Podaj prawidlowa wartosc!")
            continue
        print("Pole trojkata wynosi: ", poleTrojkata(a, h))
    elif (wybor == "4"):
        a = float(input("Podaj wartosc podstawy a: "))
        if (a <= 0):
            print("Podaj prawidlowa wartosc!")
            continue
        b = float(input("Podaj wartosc podstawy b: "))
        if (b <= 0):
            print("Podaj prawidlowa wartosc!")
            continue
        h = float(input("Podaj wartosc wysokosci h: "))
        if (h <= 0):
            print("Podaj prawidlowa wartosc!")
            continue
        print("Pole trapezu wynosi: ", poleTrapezu(a, b, h))
