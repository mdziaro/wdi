'''
Proszę napisać program, który umożliwia zamianę dowolnej liczby naturalnej
z jednego systemu liczb w drugi w zależności od wyboru użytkownika (na wejściu).
Należy rozważyć następujące systemy liczbowe: dwójkowy, ósemkowy, dziesiętny, szesnastkowy.
'''

liczba = input("Podaj liczbę, w systemie, w którym jest zapisana")
baza_pocz = int(input("Podaj system, w którym jest zapisana liczba"))
baza_konc = int(input("Podaj system, na który chcesz zamienić liczbę"))

if liczba[0] == "-" or baza_pocz < 2 or baza_pocz > 16 or baza_konc < 2 or baza_konc > 16:
    print("Wprowadzono niepoprawne dane")
    exit(0)

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

#print(BaseToTen(16, "AC3"))
def TenToBase(baza, liczba):
    wynik = []
    liczba_kopia = liczba
    while liczba_kopia>0:
        wynik.append(liczba_kopia%baza)
        liczba_kopia //= baza
    wynik = wynik[::-1]
    return wynik

def ZamianaBaz(baza_pocz, liczba, baza_konc):
    wynik=""
    tablica = TenToBase(baza_konc,BaseToTen(baza_pocz, liczba))
    for i in range(len(tablica)):
        if tablica[i] < 10:
            wynik += str(tablica[i])
        else:
            wynik += chr(tablica[i]-11 + ord("A"))
    return wynik

# sprawdzam, czy w danym systemie w ogóle istnieje taka liczba.
cyfry = []
for i in range(len(liczba)):
    cyfry.append(liczba[i])
for i in range(len(cyfry)):
    if not cyfry[i].isnumeric():
        cyfry[i] = ord(cyfry[i]) - ord("A") + 10
    if int(cyfry[i]) >= baza_pocz:
        print("Podana liczba nie istnieje w danym systemie")
        exit(0)
    else:
        continue
print(ZamianaBaz(baza_pocz, liczba, baza_konc))
