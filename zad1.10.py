a = int(input())
b = int(input())
c = int(input())

def Euklides(a,b):
    if b > a:
        a,b = b,a
    while b != 0:
        a,b = b, a % b
    return a

def NWD(a,b,c):
    return Euklides(Euklides(a,b),c)

print(NWD(a,b,c))