#나이 계산 프로그램

current_year = 2021
birth_year = int(input("태어난 년도를 입력하세요 : "))
#print(birth_year)

#나이 계산
age = (current_year - birth_year) + 1

#출력
#print(birth_year, "년에 태어난 사람의 나이는", age, "세 입니다.")
print(str(birth_year) +"년에 태어난 사람의 나이는 " + str(age)+"세 입니다.")
