import random as r

f = open('c:/web_dev/pyfile/season.txt', 'r')


#랜덤하게 자료 읽기
word = f.read().split() #공백으로 구분
w = r.choice(word)
print(w)

f.close()