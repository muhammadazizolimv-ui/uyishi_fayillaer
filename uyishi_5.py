class Mahsulot:
    def __init__(self, nomi, narxi, miqdori):
        self.nomi = nomi
        self.narxi = narxi
        self.miqdori = miqdori


n = int(input())

mahsulotlar = []

for i in range(n):
    nomi, narxi, miqdori = input().split()
    m = Mahsulot(nomi, int(narxi), int(miqdori))
    mahsulotlar.append(m)

with open("mahsulotlar.txt", "w") as fayl:
    for m in mahsulotlar:
        fayl.write(f"{m.nomi} {m.narxi} {m.miqdori}\n")
