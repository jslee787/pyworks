#리스트의 생성 및 관리
number = [10, 20, 30, 40]

#요소의 개수
len(number)
print(len(number))

#for ~ in문
for i in number:
    print(i)
print()
#for ~ range()문
n = len(number)
for i in range(0,n):
    print(number[i], end=' ')
print()

#요소 추가
number.append(50)
print(number)

#요소 수정
number[1] = 60
print(number)
print(type(number)) #자료형 list

#요소 삭제
#del number[2]  명령어 삭제
number.pop(2)   #함수 삭제
print(number)

