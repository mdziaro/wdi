import random

def kalkulator():
    a = int(input("Podaj 1. liczbę: "))
    b = int(input("Podaj 2. liczbę: "))
    dzialanie = input("jakie działanie chcesz wykonać? Wpisz +, -, *, /, #, ^ lub : ")

    if dzialanie == "+":
        print(a+b)
    elif dzialanie == "-":
        print(a-b)
    elif dzialanie == "*":
        print(a*b)
    elif dzialanie == "/":
        if b == 0:
            print("Nie można dzielić przez zero")
            koniec()
        else:
            print(a/b)
    elif dzialanie == "#":
        print("pierwiastek z pierwszej liczby:", a**(1/2), "\n","pierwiastek z drugiej liczby", b**(1/2))
    elif dzialanie == "^":
        print(a**b)
    elif dzialanie == "x":
        print(random.randint(a,b))
    koniec()


def koniec():
    czy_koniec = input("Czy chcesz wprowadzić nowe dane? Wpisz T/N")
    if czy_koniec == "T":
        kalkulator()
    elif czy_koniec == "N":
        return 0
    else:
        koniec()

print(kalkulator())