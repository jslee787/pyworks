# while ~ break 문

'''
# 1 ~ 10
i = 0
while True:
    i += 1
    if i>10:
        break
    print(i)
'''

#키가 'y'이면 "계속 반복", 'n'이면 "반복 중단", 그 이외의 키는 "정상 답변이 아님"
while True:
    key = input("반복을 계속 할까요?(y/n) : ")

    #조건 처리
    if key == 'y' or key =='Y' :
        print("계속 반복합니다.")
    elif key == 'n' or key =='N':
        print("반복을 중단합니다.")
        break
    else:
        print("정상적인 답변이 아닙니다.")
