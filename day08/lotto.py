#로또 복권 생성 프로그램
#1~45 중에 추첨
import random

lotto = []  #빈 리스트 준비

#로또 복권 번호 1개 추첨
'''
for i in range(6):      #0~5
    num = random.randint(1, 45)
    if num not in lotto:    #기존 리스트에 없는 번호일때
        #print(num, end= ' ')
        lotto.append(num)   #리스트에 num 추가
'''

while len(lotto) < 6 :  #0~5 => 6개
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)

print(lotto)