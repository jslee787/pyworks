#구구단 파일 쓰기
#with ~ as 구문 -> f.close()를 사용하지 않음
with open('99.text', 'w') as f:     #추가 쓰기 - 'a' 모드
    dan = 11
    for i in range(1, 10):
        f.write('%d * %d = %d\n' % (dan, i, dan * i))
    f.write('\n')