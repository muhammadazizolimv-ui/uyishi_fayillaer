class Avtomobil:
    def __init__(self, marka, yil, narx):
        self.marka = marka
        self.yil = yil
        self.narx = narx


n = int(input())

avtomobillar = []

for i in range(n):
    marka, yil, narx = input().split()
    a = Avtomobil(marka, int(yil), int(narx))
    avtomobillar.append(a)

with open("avtomobillar.txt", "a") as fayl:
    for a in avtomobillar:
        fayl.write(f"{a.marka} {a.yil} {a.narx}\n")
