#재귀함수 = 자기가 자신을 호출하는 함수
def sos2(n):
    print('Help me!!')
    if n < 1:
        return ""
    else:
        return sos2(n-1)

#sos1(5)
sos2(5)