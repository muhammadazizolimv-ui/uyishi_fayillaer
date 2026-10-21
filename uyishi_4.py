class Talaba:
    def __init__(self, ism, yosh, ball):
        self.ism = ism
        self.yosh = yosh
        self.ball = ball

n = int(input())

talabalar = []

for i in range(n):
    ism, yosh, ball = input().split()
    t = Talaba(ism, int(yosh), int(ball))
    talabalar.append(t)

with open("talabalar.txt", "w") as fayl:
    for t in talabalar:
        fayl.write(f"{t.ism} {t.yosh} {t.ball}\n")
