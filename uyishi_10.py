class Xodim:
    def __init__(self, ism, yosh, oylik):
        self.ism = ism
        self.yosh = yosh
        self.oylik = oylik


ism, yosh, oylik = input().split()

x = Xodim(ism, int(yosh), int(oylik))

with open("xodimlar.txt", "a") as fayl:
    fayl.write(f"{x.ism} {x.yosh} {x.oylik}\n")
