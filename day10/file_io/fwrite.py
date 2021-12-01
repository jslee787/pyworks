#파일 쓰기

f = open("c:/web_dev/pyfile/file.txt", 'w') #파일열기 - 쓰기모드
f.write('하늘이 파랗다.\n')
f.write('Thank you!!!\n')
f.write('社員\n')
#f.write(45)

f.close()       #파일 닫기