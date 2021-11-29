#Counter 클래스 만들기
#인스턴스 변수

class Counter:
    def __init__(self):
        self.x = 0      #시작 0으로 초기화(인스턴스 변수)
        self.x += 1     #1 증가

    def getcount(self):
        return self.x

c1 = Counter()      #c1 은 인스턴스 객체
print(c1.getcount())

c2 = Counter()
print(c2.getcount())

c3 = Counter()
print(c3.getcount())