class Talaba:
    def __init__(self, ism, yosh, ball):
        self.ism = ism
        self.yosh = yosh
        self.ball = ball


ism, yosh, ball = input().split()

t = Talaba(ism, int(yosh), int(ball))

with open("talabalar.txt", "a") as fayl:
    fayl.write(f"{t.ism} {t.yosh} {t.ball}\n")
