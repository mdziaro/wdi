liczba =int(input())
import random
def choinka(a):
    print(" "*((a-1)), "X")
    a *= 2
    for i in range(3, a, 2):
        m = random.randint(1,i)
        print(" "*(((a-i)//2)), (i-m)*"*" + "o" + "*"*(m-1))
    print(" " * ((a-1)//2), "U")
choinka(liczba)