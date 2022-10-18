saldo = 10000
PIN = 123456


def wybor1():
    print("Chcesz dokonać Wpłaty (WP), Wypłaty (WY), Sprawdzić Saldo (S), czy wyjść? (E)")
    wybor = input("Wpisz WP/WY/S/E")
    if wybor == "E":
        print("Koniec Transakcji")
        return 0
    sprawdzpin(wybor, saldo)

def wybor2(saldo):
    print("Co chcesz zrobić w kolejnym kroku?")
    wybor = input("Wpisz WP/WY/S/E")
    if wybor == "E":
        print("Koniec Transakcji")
        return 0
    sprawdzpin(wybor, saldo)


def sprawdzpin(wybor, saldo):
    check_pin = int(input("Wprowadź PIN:"))
    if check_pin == PIN:
        print("Wprowadzono poprawny PIN.")
        dzialanie(wybor, saldo)
    else:
        print("Wprowadzono niepoprawny PIN")
        wybor2(saldo)


def dzialanie(wybor, saldo):
    if wybor == "WY":
        kwota = int(input("Wprowadź kwotę, którą chcesz wypłacić:"))
        if kwota > saldo:
            print("Niewystarczające środki na koncie")
            wybor2(saldo)
        else:
            print("Wypłacono", kwota, "zł.")
            saldo -= kwota
            wybor2(saldo)
    elif wybor == "WP":
        kwota = int(input("Wprowadź kwotę, którą chcesz wpłacić:"))
        saldo += kwota
        wybor2(saldo)
    elif wybor == "S":
        print("Twój stan konta to", saldo)
        wybor2(saldo)
    else:
        print("Niepoprawna komenda.")
        wybor2(saldo)


wybor1()