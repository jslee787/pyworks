#while 반복문
#1~10 출력
i = 0
sum_v = 0
while i <10:
    i += 1  # i = i + 1
    sum_v += i
    #print(i)

print("i의 값 : ", i)
print("sum = ", sum_v)
#1~10 짝수 출력
i=0
while i <10:
    i += 1
    if i % 2 == 0:
        print(i, end=' ')
