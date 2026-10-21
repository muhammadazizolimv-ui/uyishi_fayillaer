class Mahsulot:
    def __init__(self, nomi, narxi, miqdori):
        self.nomi = nomi
        self.narxi = narxi
        self.miqdori = miqdori


nomi, narxi, miqdori = input().split()

m = Mahsulot(nomi, int(narxi), int(miqdori))

with open("mahsulotlar.txt", "a") as fayl:
    fayl.write(f"{m.nomi} {m.narxi} {m.miqdori}\n")
