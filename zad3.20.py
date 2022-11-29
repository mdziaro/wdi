import os
import hashlib

plik = open("/home/my_hashed_password.txt")
hasla = plik.readlines()
plik.close()



def logowanie():
    user = input("Podaj nazwę użytkownika: ")
    haslo = input("Podaj hasło: ")
    print(hasla)



def przywitanie():
    print("Witaj. Co chcesz zrobić? \n")
    wybor = input("1. Zmienić nazwę pliku. \n2. Skopiować plik do innego miejsca. \n3. Przenieść plik. \n4. Usunąć plik.\n5. Wylogować się. \nWpisz cyfrę, by wybrać: ")
    if wybor == "1":
        nazwa()
    if wybor == "2":
        kopiowanie()
    if wybor == "3":
        przenoszenie()
    if wybor == "4":
        usuwanie()
    if wybor == "5":
        exit("Użytkownik wylogowany.")
    else:
        print("Nie rozumiem tej komendy.")
        przywitanie()

def nazwa():
    pass
    return
logowanie()