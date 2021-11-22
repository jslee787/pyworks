#find() 함수 - 문자의 위치 확인
s = "Hello, welcome to my website!"
print(s.find('H'))
print(s.find('ll'))
print(s.find('k'))  #찾는 문자가 없으면 -1

s = s.find("welcome")   #단어로 검색 : 첫번째 글자 위치
print(s)

#strip()함수 -공백제거
str1 = "  hi, soo!"
print(str1.strip())
print(str1.lstrip())    #left strip()

txt = "    banana    "
x = txt.strip()
print("Of all fruits", x, "is my favorite")

#isnumeric() - 숫자인지 검사하는 함수
text = "123".isnumeric()
print(text)

text2 = "123ab".isnumeric()
print((text2))
