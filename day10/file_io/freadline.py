#파일 읽기

f = open('c:/web_dev/pyfile/season.txt', 'r') #파일 읽기 모드
#seasons = f.readline()
#print(seasons)
seasons = f.readlines()
print(seasons)
#print(seasons[0])
#print(seasons[-1])

#전체 읽기
for season in seasons:
    #print(season)
    print(season.strip())   #한줄공백제거


f.close()