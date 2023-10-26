"""
Készíts eljárást, mely a paramterében kap egy számot. 
Az eljárás írja ki a hárommal osztható számokat eddig a számig vesszővel elválasztva.  
Az utolsó szám után ne legyen jel! 
"""
def feladat1( a:int ):
        i = 1
        while i <= a:
            if i % 3 == 0:
                if i == a or i + 3 > a:
                    print(i)
                else:
                    print(i, end=", ")
            i += 1

"""
Készíts eljárást, mely a paraméterében kap egy pozitív egész számot. 
Az eljárás írja ki a számokat a képernyőre ;-vel elválasztva csökkenő sorrendben 1-ig! Az utolsó szám után ne legyen pontosvessző!  
Pl.: ha a szám 5 
5; 4; 3; 2; 1 
"""
def feladat2(a: int):
    i = a
    while i >= 1:
        if i == 1:
            print(i)
        else:
            print(i, end="; ")
        i -= 1

"""
Kérjünk be a felhasználótól 5-tel osztható számot! A számot addig kérjük be, amíg nem sikerül 5-tel oszthatót beírnia!  
"""
def feladat3(a:int):
    while a % 5 != 0:
        print("Öttel oszthato szamot adj meg!")
        return
    else:
        print(f"{a} öttel osztható!")

"""
Készíts eljárást, mely a paramterében kap egy számot. Az eljárás írja ki a számokat eddig a számig,  
ha a szám 3-mal osztható, akkor ne a számot írja ki, hanem írja helyette, hoyg BUMM. 
Az utolsó szám után ne legyen vessző! Pl, ha a szam=7  1, 2, BUMM, 4, 5, BUMM, 7 
Egészítsd ki a feladatot, hogy ha páros szám, akkor BAM-ot írjon, és ha 3-mal és 2-vel is osztható, akkor BUMMBAM-ot írjon! 
1, BAM, BUMM, BAM, 5, BUMMBAM, 7 
"""
def feladat4(a:int):
    if (a<=0):
        print("Hiba!")
        return
    i = 1
    while i <= a:
        if i % 3 == 0 and i % 2 == 0:
            if i == a:
                print(i)
            else:
                print("BUMMBAM", end=", " )
        elif i % 3 == 0:
            if i == a:
                print(i)
            else:
                print("BUMM", end=", ")
        elif i % 2 == 0:
            if i == a:
                print(i)
            else:
                print("BAM", end=", ")
        else:
            if i == a:
                print(i)
            else:
                print(i, end=", ")
        i += 1

