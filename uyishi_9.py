class Xodim:
    def __init__(self, ism, yosh, oylik):
        self.ism = ism
        self.yosh = yosh
        self.oylik = oylik


n = int(input())

xodimlar = []

for i in range(n):
    ism, yosh, oylik = input().split()
    x = Xodim(ism, int(yosh), int(oylik))
    xodimlar.append(x)

with open("xodimlar.txt", "w") as fayl:
    for x in xodimlar:
        fayl.write(f"{x.ism} {x.yosh} {x.oylik}\n")
