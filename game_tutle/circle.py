#여러개의 원 그리기
import turtle as t

t.shape('turtle')
t.color('blue')
t.bgcolor('beige')


n = 200
t.speed(0)  #1~10  가장 빠른속도 = 0
for i in range(n):
    t.circle(100)
    t.left(360/n)       #7.5

t.mainloop()