"""
Napisz program, który utworzy i wypisze listę składającą się z N liczb z przedziału[1,100],
a następnie po każdej liczbie pierwszej wstawi nowy element o wartości 0.
Następnie program powinien policzyć sumy podzbiorów znajdujących się pomiędzy zerami.
Lista przed modyfikacją:[7,45,45,34,53,45,4,3,11,18].
Lista po modyfikacji: [7,0,45,45,34,53,0,45,4,3,0,11,0,18,30].
Wynik:7;177;52;11;48.

"""
import random

if __name__ == "__main__":
    def SitoErastostenesa(przedzial_gora):
        pierwsze = [True] * (przedzial_gora + 1)
        pierwsze[0] = False
        pierwsze[1] = False
        for i in range(2, przedzial_gora // 2):
            if pierwsze[i]:
                for j in range(i * 2, przedzial_gora + 1, i):
                    pierwsze[j] = False
        return pierwsze

    """
    jeżeli liczba jest pierwsza, to pierwsze[liczba] jest równe True
    algorytm jest nieoptymalny gdy przedział dolny jest większy od 1,
    lub gdy przedział liczb jest duży w porównaniu do długości tablicy

    """

    def Czy_Pierwsza(liczba):
        if liczba % 2 == 0 or liczba % 3 == 0:
            return False
        else:
            i = 5
            while i < liczba**(1/2) + 1:
                if liczba%(i) == 0 or liczba%(i+2) == 0:
                    return False
                else:
                    i += 6
            return True

    #Dla krótkich list o dużych wartościach bardziej wydajna będzie funkcja Czy_Pierwsza

    def Suma_Podzbiorow(tablica):
        wynik = [0]
        indeks_wyniku = 0
        for i in range(len(tablica)):
            if tablica[i] == 0:
                indeks_wyniku += 1
                if len(tablica) != i+1:
                    wynik.append(0)
            else:
                wynik[indeks_wyniku] += tablica[i]
        return wynik
    


    #tworzenie tablicy
    przedzial_dol = 1
    przedzial_gora = 100
    dlugosc = int(input("Wpisz długość listy:" + "\n"))
    if dlugosc <= 0:
        print("długość tablicy musi być dodatnią liczbą naturalną")
        exit()
    tablica = [random.randint(przedzial_dol, przedzial_gora) for i in range(dlugosc)]

    sito = SitoErastostenesa(przedzial_gora)
    tablica_z_zerami = []
    for i in range(len(tablica)):
        tablica_z_zerami.append(tablica[i])
        #if Czy_Pierwsza(tablica[i]):
        #    tablica_z_zerami.append(0)
        if sito[tablica[i]]:
            tablica_z_zerami.append(0)

    print(Suma_Podzbiorow(tablica_z_zerami))

#[7,45,45,34,53,45,4,3,11,18] -> [7,177,52,11,18]
#[83,18,68,44,4,60,53,93,78,83] -> [83,247,254]
# dla nienaturalnej  długości tablicy obsługuje błąd



