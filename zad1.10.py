a = int(input("Wpisz pierwszą liczbę:"))
b = int(input("Wpisz drugą liczbę:"))
c = int(input("Wpisz trzecię liczbę:"))

def Euklides(a,b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def NWD(a,b,c):
    return Euklides(Euklides(a,b),c)

print(NWD(a,b,c))