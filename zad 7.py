lewy_brzeg = float(input("Podaj lewy brzeg zakresu(liczba całkowita)" + "\n"))
prawy_brzeg = float(input("Podaj prawy brzeg zakresu(liczba całkowita)" + "\n"))
def sposob_pierwszy(lb,pb):
    odp = []
    if lb % 1 != 0 or pb %1 != 0:
        print("Podane liczby nie są całkowite")
    if pb < lb:
        print("Podano zakres o ujemnej długości")
    lb = int(lb)
    pb = int(pb)
    if pb-lb+1 > 20:
        if ((pb-lb) % 2) == 0:
            for i in range(int((pb+lb)/2)-2,int((pb+lb)/2)):
                odp.append(i)
            for i in range(int((pb+lb)/2)+1,int((pb+lb)/2)+4):
                odp.append(i)

    #jeśli zakres ma nieparzystą długość,
    #to średnia jest jedną z liczb w tym zakresie.
    #Stąd musimy pominąć (pb+lb)/2

        else:
            for i in range(int((pb+lb)/2)-2,int((pb+lb)/2)+4): #przy parzystej długości nie ma tego problemu
                odp.append(i)
            odp.pop(0)

    else:
        for i in range(lb, pb+1):
            odp.append(i)
    return odp

# Sposób drugi:
def sposob_drugi(lb,pb):
    if lb % 1 != 0 or pb %1 != 0:
        print("Podane liczby nie są całkowite")
    if pb < lb:
        print("Podano zakres o ujemnej długości")
    odp = []
    len = pb-lb+1
    i = 6
    if len > 20:
        while i > 0:
            odp.append(int(((int(pb+lb)/2)+4)-i))
            i -= 1
        if (pb+lb)/2 in odp:
            odp.remove((pb+lb)/2)
            return odp
        else:
            odp.pop(0)
            return odp
        # tutaj robię to mądrzej, i po prostu usuwam wartość z listy, jeżeli jest równa średniej zakresu

print(sposob_pierwszy(lewy_brzeg,prawy_brzeg))
print(sposob_drugi(lewy_brzeg,prawy_brzeg))

