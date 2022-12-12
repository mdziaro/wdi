import os
import hashlib

with open('home/my_hashed_password.txt') as f:
    user_list = [tuple(map(str, i.split(' '))) for i in f]


def logowanie():
    username = input("Podaj nazwę użytkownika: ") # user - password || admin - admin
    password = hashlib.sha256()
    haslo = input("Podaj hasło: ")
    password.update(bytes(haslo, 'utf-8'))
    password = password.hexdigest()
    for user in range(len(user_list)):
        if user_list[user][0] == username:
            if user_list[user][1][:-1] == password:
                print("Zalogowano pomyslnie")
                przywitanie()
            else:
                break
    print("Nazwa użytkownika lub hasło są nieprawidłowe.")
    logowanie()



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
    path = input("Podaj ścieżkę pliku, którego nazwę chcesz zmienić (destination/file.ext): ")
    name = input("Jaką nazwę chcesz nadać plikowi? (pamiętaj o rozszerzeniu!) ")
    command = str("rename " + path + " " + name)
    os.system(command)
    print("Operacja ukończona pomyślnie!\n\n")
    przywitanie()

def kopiowanie():
    path = input("Podaj ścieżkę pliku, który chcesz skopiować (destination/file.ext): ")
    path2 = input("Podaj ścieżkę folderu, do którego chcesz skopiować plik (destination/: ")
    name = input("Podaj nową nazwę pliku (file.ext): ")
    command = str("copy " + path + " " + path2+name)
    print(command)
    os.system(command)
    print("Operacja ukończona pomyślnie!\n\n")
    przywitanie()

def przenoszenie():
    path = input("Podaj ścieżkę pliku, który chcesz przenieść (destination/file.ext: ")
    path2 = input("Podaj ścieżkę docelową ścieżkę pliku (destination/file.ext: ")
    os.replace(path, path2)
    print("Operacja ukończona pomyślnie!\n\n")
    przywitanie()

def usuwanie():
    path = input("Podaj ścieżkę pliku, który chcesz usunąć (destination/file.ext: ")
    os.system("del " + path)
    print("Operacja ukończona pomyślnie!\n\n")
    przywitanie()

logowanie()
