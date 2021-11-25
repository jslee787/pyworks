#random 모듈 사용하기
import random

#주사위 10번 던지기

for x in range(10):
    dice = random.randint(1, 6)
    print(dice)

print("=" * 30)

#주사위 2개를 만들어서 합계 구하기 + 눈이 같으면 "Double!!" 출력
for x in range(10):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(total)

    if dice1 == dice2:
        print("Double!!")