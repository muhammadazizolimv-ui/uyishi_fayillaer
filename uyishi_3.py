class Avtomobil:
    def __init__(self, marka, yil, narx):
        self.marka = marka
        self.yil = yil
        self.narx = narx

marka = input()
yil = int(input())
narx = int(input())

a = Avtomobil(marka, yil, narx)

with open("avtomobil.txt", "w") as fayl:
    fayl.write(a.marka + "\n")
    fayl.write(str(a.yil) + "\n")
    fayl.write(str(a.narx) + "\n")
