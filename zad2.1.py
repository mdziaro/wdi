'''
Proszę napisać program, który umożliwia zamianę dowolnej liczby naturalnej
z jednego systemu liczb w drugi w zależności od wyboru użytkownika (na wejściu).
Należy rozważyć następujące systemy liczbowe: dwójkowy, ósemkowy, dziesiętny, szesnastkowy.
'''

def BaseToTen(baza, liczba):
    wynik = 0
    iteracja = 0
    kopia_liczba = str(liczba).upper()
    while len(kopia_liczba) > 0:
        if kopia_liczba[-1].isnumeric():
            wynik += (int(kopia_liczba[-1]) * (baza**iteracja))
        else:
            wynik += (10 + ord(kopia_liczba[-1]) - ord("A"))*(baza**iteracja)
            # W ASCII, kolejne litery A,B,C... mają przypisane kolejne, rosnące wartości.
            # Uzyskuję miejsce litery w alfabecie poprzez różnicę jej wartości od wartości pierwszej litery alfabetu
        iteracja += 1
        kopia_liczba = kopia_liczba[:-1]
    return wynik

print(BaseToTen(13, "AC3"))
def TenToBase
