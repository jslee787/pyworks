#주요 내장 함수
#all(x) - 리스트 안에 0이 있으면 False, 없으면 True
print(all([1,2,3]))     #True
print(all([1,0,3]))     #False

#any(x) - 반복 자료 안에 모두 0일때만 False, 나머지는 True
print(any([1,0,3]))     #True

#eval - 문자열 표현 -> 숫자로 변환
print(eval("1+2"))      #3

#list() - 자료를 리스트로 반환
print(list('python'))

#절대값
print(abs(-10))

#반올림
print(round(4.7))
print(round(4.52))
print(round(4.32))

#합계
print(sum([1,2,3,4]))

#최소값
print(min([1,2,3,4]))

#거듭제곱
print(pow(2,4))