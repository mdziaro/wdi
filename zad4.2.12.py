def hanoi(dysk, poz1, poz2, poz3):
    if dysk == 1:
        print("Przesuń dysk z wieży", poz1, "do wieży ", poz3)
    else:
        hanoi(dysk-1, poz1,poz3,poz2)
        print("Przesuń dysk z wieży", poz1, "do wieży ", poz3)
        hanoi(dysk-1,poz2,poz1,poz3)

poz1 = 1
poz2 = 2
poz3 = 3
dysk = int(input("Ile dysków rozważyć?"))
print(hanoi(dysk, poz1, poz2, poz3))