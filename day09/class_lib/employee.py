#Employee 클래스 정의
from day09.class_lib.person import Person

class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)     #부모멤버 super함수 사용
        self.employeeID = employeeID    #자기멤버초기화

    def __str__(self):
        return super().__str__() + ", 사번 : " + str(self.employeeID)
e = Employee("이강", 25, 101)
print(e)
'''
print("이름 : " + e.name)
print("나이 : " + str(e.age))
print("사번 : " + str(e.employeeID))
'''