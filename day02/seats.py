#자리 배치도 프로그램
#고객 수를 열(좌석)로 눠서 행(줄)을 구해서 for문으로 배치

customer = int(input("입장객수 입력: "))
col = int(input("좌석 열 수 입력: "))

#나머지가 없는 경우 있는 경우로 row 계산
if customer % col == 0:
    row = customer // col
else:
    #row = customer // col + 1
    row = int(customer / col) + 1

for i in range(0, row):
    for j in range(1, col+1):
        seat = i*col+j
        if seat > customer:
            break
        print('좌석' + str(seat), end=' ')
    print()
