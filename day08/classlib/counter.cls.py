#클래스 변수 - 인스턴스 변수와 대응하는 개념

class Counter:
    x = 0   #클래스 변수(self를 사용하지 않음)

    def __init__(self):
        Counter.x += 1

    def getcount(self):
        return Counter.x

c1 = Counter()
print(c1.getcount())

c2 = Counter()
print(c2.getcount())

c3 = Counter()
print(c3.getcount())