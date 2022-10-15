a = int(input("Podaj pierwszą liczbę:" + "\n"))
b = int(input("Podaj drugą liczbę:" + "\n"))
""" 
znak "\n" sprawia, że wpisana liczba 
nie pojawia się w tym samym wierszu, co pytanie

"""
if a< 0 and b< 0:
    print("obie liczby są mniejsze od zera, program zostanie zakończony")
elif a*b <0: #jeśli iloczyn dwóch liczb jest mniejszy od zera, to jedna z nich jest ujemna
    a = abs(a)
    b = abs(b)
print("suma tych liczb to", a+b)
print("różnica tych liczb to", a-b)
print("iloczyn tych liczb to", a*b, "Yay!" if a*b == 10 else "")
print("iloraz tych liczb to", a/b)
print("kwadrat liczby pierwszej to", a**2)
print("kwadrat liczby drugiej to", b**2)
print("pierwiastek liczby pierwszej to", a**(1/2))
print("pierwiastek liczby drugiej to", b**(1/2))