#리스트의 복사
a1 = [1, 2, 3, 4]
a2 = []     #빈 리스트 생성하기
a3 = []
# a1 에 5를 저장
a1.append(5)
print(a1)

#복사 저장 (a1 -> a2로 복사)
for i in a1:
    #a2.append(i)
    a2.append(i * 2) #2의 배수
print(a2)

#a3에 a1 홀수만 저장
for i in a1:
    if i % 2 == 1:
        a3.append(i)
print(a3)