#전역변수 - global 키워드

def one_up():
    global x       #지역변수, 블럭을 벗어나면 메모리에서 해제
    x += 1
    return x

x = 1           #전역변수, 프로그램이 종료될 때 메모리에서 해제
print(one_up()) #2
print(one_up()) #3
print(one_up()) #4
#print(x)