#Dog 클래스 만들기
class Dog:
    kind = '진돗개'    #클래스변수

    def __init__(self, name):
        self.name = name    #인스턴스 멤버 변수

dog1 = Dog('백구')
dog2 = Dog('흰둥이')

print(dog1.name)
print(dog1.kind)
print(dog2.name)
print(dog2.kind)