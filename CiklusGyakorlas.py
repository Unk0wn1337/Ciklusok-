def elsoFeladat():
    szam:int = int(input("Szeretnek kerni egy számot: "))
    index:int = 0
    while index < szam:
        if index < szam:
            print(index,end=",")
        else:
            print(index,end=" ")
        index+=1
    print(index)

def masodikFeladat():
    szam:int = int(input("Szeretnek kerni egy számot:  "))
    osszeg:int = 0
    index:int = 0
    while index < szam:
        if index % 2 == 0:
            print(f"Osztható számok: {index}")
            osszeg += index
            print(f"Oszthatói összege:{osszeg}")
        index+=1
def harmadikFeladat():
    szam:int = int(input("Szeretnek kerni egy számot:  "))
    index = 0
    while index < szam:
        print(index,end=",")
        index+=2
def negyedikFeladat():
    szam = 20
    index = 0
    while index < szam:
        negyzetSzam = index**2
        if index < szam -1:
            print(negyzetSzam,end=",")
        else:
            print(negyzetSzam,end=" ")
        index+=1
def otodikFeladat():
    szoveg:str = input("Kerek egy szoveget: ")
    index:int = 0
    while index < len(szoveg):
        print(szoveg[index])
        index+=1

def hatodikFeladat():
    szoveg: str = input("Kerek egy szoveget: ")
    index:int = len(szoveg)-1
    while not index  < 1:
        print(szoveg[index])
        index-=1
    print(szoveg[index], end="")

def hetedikFeladat():
    m:int = int(input("Kére egy m-et"))
    n: int = int(input("Kérek egy n-et"))
    print("*"*m,end="")
    index = 0
    hossz = m-2
    jel="*"
    while index <= n:
        print(f"{jel:^{hossz}}{jel}")
        index+=1

