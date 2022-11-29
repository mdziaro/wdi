import random

def tworzenie_macierzy(dotychczasowa_macierz, nr_wiersza):
    nr_wiersza += 1
    wiersz = input("Wypisz liczby w "+ str(nr_wiersza)+ " wierszu macierzy, oddzielając liczby przecinkiem: ")
    wiersz = wiersz.split(",")
    dotychczasowa_macierz.append(wiersz)
    wybor = input("Czy chcesz dodać nowy wiersz? Wpisz T/N: ")
    if wybor == "T":
        tworzenie_macierzy(dotychczasowa_macierz, nr_wiersza)
    else:
        return dotychczasowa_macierz
    return dotychczasowa_macierz

def sprawdzanie_dlugosci_macierzy(macierz):
    if len(macierz) > 1:
        for i in range(len(macierz) - 1):
            if  len(macierz[i]) == len(macierz[i + 1]):
                i += 1
            else:
                print("Podane wiersze nie tworzą macierzy!")
                exit()
    else:
        return True
    return True

#print("Stwórz pierwszą macierz!")
#macierz1 = tworzenie_macierzy([],0)
#sprawdzanie_dlugosci_macierzy(macierz1)
#print("Stwórz drugą macierz!")
#macierz2 = tworzenie_macierzy([],0)
#sprawdzanie_dlugosci_macierzy(macierz2)

#macierz1 = [
#['1', '3', '4'],
#['1', '1', '1'],
#['1', '2', '3']
# ]
#macierz2 = [
# ['2', '3', '4','2'],
# ['1', '3', '1','4'],
# ['1', '2', '3','4']
# ]


macierz1 = [
    [1, 1, 0],
    [1, 0, 1],
    [1, -1, -1]
]

macierz2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

def zmien_znaki_na_liczby(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            macierz[i][j] = int(macierz[i][j])
    return macierz

macierz1 = zmien_znaki_na_liczby(macierz1)
macierz2 = zmien_znaki_na_liczby(macierz2)
#########################################
dlugosc1 = len(macierz1[0])
wysokosc1 = len(macierz1)
dlugosc2 = len(macierz2[0])
wysokosc2 = len(macierz2)
def iloczyn(tab1, tab2):
    wynik = [[0 for _ in range(dlugosc2)] for _ in range(wysokosc1)]
    for i in range(wysokosc1):
        for j in range(dlugosc2):
            for k in range(wysokosc2): #wysokosc2 = dlugosc1
                wynik[i][j] += tab1[i][k]*tab2[k][j]

    return wynik


def calc_det(matrix):
    def calc_det_recur(matrix, y, il, poss, perm, inv):
        if y >= len(matrix):
            # print("-----\nend, il:", il)
            nonlocal su

            if inv % 2 == 0:
                modif = 1
            else:
                modif = -1

            su += modif * il
            # print("sum", su,"\n-------\n")
            return il

        for curr_i in poss:
            # print("y", y)
            # print("curr_i", curr_i, [i for i in poss if i != curr_i])

            inv_c = inv
            for perm_el in perm:
                if perm_el > curr_i:
                    inv_c += 1

            calc_det_recur(matrix, y + 1, il * matrix[y][curr_i], [i for i in poss if i != curr_i], perm + [curr_i],
                           inv_c)

    su = 0
    poss = [i for i in range(len(matrix))]
    for curr_i in range(len(matrix[0])):
        # print("y", 0)
        # print("curr_i", curr_i, [i for i in poss if i != curr_i])
        calc_det_recur(matrix, 1, matrix[0][curr_i], [i for i in poss if i != curr_i], [curr_i], 0)

    return su

def mnozenie_skalarne(macierz, skalar):
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            macierz[i][j] = skalar * macierz[i][j]
    return macierz

print("Iloczyn tych macierzy to: " + str(iloczyn(macierz1, macierz2)))
wyznacznik1 = calc_det(macierz1)
wyznacznik2= calc_det(macierz2)
print("Wyznacznik pierwszej macierzy to: " + str(wyznacznik1))
print("Wyznacznik drugiej macierzy to: " + str(wyznacznik2))
suma_wyznacznikow = wyznacznik1+wyznacznik2
print("Pierwsza macierz pomnożona przez sumę wyznaczników to: " + str(mnozenie_skalarne(macierz1,suma_wyznacznikow)))
print("Druga macierz pomnożona przez sumę wyznaczników to: " + str(mnozenie_skalarne(macierz2,suma_wyznacznikow)))
