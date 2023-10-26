import ciklusok

print("Teszteset 1 - páros szám, amely 3-al nem oszahtó: 4 ")
print("Várt eredmény: 1, BAM, BUMM, BAM")
ciklusok.feladat4(4)

print("Teszteset 1 - 6-tal osztható szám => 2-vel és 3-al is osztató lesz: 6 ")
print("Várt eredmény: 1, BAM, BUMM, BAM, 5, BUMMBAM")
ciklusok.feladat4(6)

print("Teszteset 1 - 3-mal osztató, de 2-vel nem: 9")
print("Várt eredmény: 1, BAM, BUMM, BAM, 5, BUMMBAM, 7, BAM, BUMM")
ciklusok.feladat4(9)

print("Teszteset 1 - se 3-al, se 2-vel nem osztató: 11")
print("Várt eredmény: 1, BAM, BUMM, BAM, 5, BUMMBAM, 7, BAM, BUMM, BAM, 11")
ciklusok.feladat4(11)

print("Teszteset 1 - negatív szám esetén:")
print("Várt eredmény: Hiba!")
ciklusok.feladat4(-7)

print("Teszteset 2 - ha nulla a paraméter:")
print("Várt eredmény: Hiba!")
ciklusok.feladat4(0)

print("Teszteset 3 - tört szám esetén:")
print("Várt eredmény: 1, BAM, BUMM, BAM, 5, BUMMBAM ")
ciklusok.feladat4(6.4)

print("Teszteset 4 - nem adok meg paramétert:")


