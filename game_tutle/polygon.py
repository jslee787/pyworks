#다각형 그리기
import turtle as t

t.shape('turtle')

def polygon(n):             #n = 변의 수
    for x in range(n):
        t.forward(50)
        t.left(360/n)


def polygon2(n, d):         #d = 거리
    for x in range(n):
        t.forward(d)
        t.left(360/n)


polygon(3)
polygon(5)

t.up()          #선 올리기(투명)
t.forward(150)
t.down()        #선 내리기(다시 보이기)

polygon2(3, 100)
polygon2(5, 100)
polygon2(7, 100)

t.mainloop()