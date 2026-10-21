class Mahsulot:
    def __init__(self, nomi, narxi, miqdori):
        self.nomi = nomi
        self.narxi = narxi
        self.miqdori = miqdori

nomi = input()
narxi = int(input())
miqdori = int(input())

m = Mahsulot(nomi, narxi, miqdori)

with open("mahsulot.txt", "w") as fayl:
    fayl.write(m.nomi + "\n")
    fayl.write(str(m.narxi) + "\n")
    fayl.write(str(m.miqdori) + "\n")
