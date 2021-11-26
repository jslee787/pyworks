import turtle

turtle.shape('turtle')
'''
turtle.forward(100) #100픽셀만큼 앞으로 이동
turtle.left(90)     #머리 방향을 왼쪽으로 90도 회전
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
'''

#for 반복문
#사각형
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

#삼각형
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
    
#원
turtle.circle(50)   #반지름 50인 원

turtle.mainloop()