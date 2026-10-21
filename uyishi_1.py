class Talaba:
    def __init__(self, ism, yosh, ball):
        self.ism = ism
        self.yosh = yosh
        self.ball = ball

ism = input()
yosh = int(input())
ball = int(input())

t = Talaba(ism, yosh, ball)

with open("talaba.txt", "w") as fayl:
    fayl.write(t.ism + "\n")
    fayl.write(str(t.yosh) + "\n")
    fayl.write(str(t.ball) + "\n")
