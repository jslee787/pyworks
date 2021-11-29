#거북이 대포 게임
#각도를 맞춰 대포를 발사해 목표지점을 맞히는 게임
import turtle as t
import random as r
#좌표 이동
'''
t.up()
t.goto(0 ,200)  #x좌표 :0 , y좌표:200
t.goto(0 ,-200)  #x좌표 :0 , y좌표:-200
t.goto(200 ,0)  #x좌표 :200 , y좌표:0
t.goto(-200 ,0)  #x좌표 :-200 , y좌표:0
'''
def turn_up():  #위쪽 화살키를 누르면
    t.left(2)   #거북이 왼쪽으로 2도 돌림

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()   #거북이가 바라보는 각도

    while t.ycor() > 0 :#거북이의 y좌표가 0보다 크면(땅 위에 있는 동안)
        t.forward(15)
        t.right(5)      #오른쪽으로 5도 돌림

    #while 반복문을 빠져 나오면 땅에 닿은 상태임
    d = t.distance(target, 0)   #거북이와 목표 지점과의 거리 저장
    t.sety(r.randint(10, 100))  #성공 또는 실패를 표시할 위치 지정
    if d<25:
        t.color('blue')
        t.write("Good!", False, "center", ("", 15)) #명중처리
        #글자쓰기 함수("문자열", 위치 이동 않음, 가운데 정렬, 글꼴 크기)
    else:
        t.color('red')
        t.write("Bad!", False, "center", ("", 15)) #실패처리
        t.color('black')
        t.goto(-200, 10)    #처음 위치로
        t.setheading(ang)   #처음 각도로

#땅 그리기
t.goto(-300, 0)
t.goto(300, 0)

#목표 지점 그리기
target = r.randint(50, 150) #목표지점을 50~150 사이의 임의의 수로 지정
t.color('green')
t.pensize(2)
t.up()
t.goto(target - 25, 2)  #x좌표, y좌표 : 2
t.down()
t.goto(target + 25, 2)

#거북이 처음 위치 설정
t.color('black')
t.up()
t.goto(-200, 10)
t.setheading(20)

#동작설정
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(fire, "space")
t.listen()

t.mainloop()