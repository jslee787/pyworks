#변수값 교환
#대입 연산자 이해
#변수 z를 사용해서 교환하기

x = 1
y = 2

print("=======교환 전=======")
print("x =", x, ", y =", y)
'''
#교환 처리

z = x
x = y
y = z
'''
#파이썬 교환 방식
x, y = y, x
print() #한줄 공백
print("=======교환 후=======")
print("x =", x, ", y =", y)
