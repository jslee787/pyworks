import sqlite3

def select_emp():
    conn = sqlite3.connect("c:/pydb/dbworks/mydb.db")   #db 연결 객체 생성
    cur = conn.cursor() #db 작업 객체
    sql = "SELECT * FROM employee"   #db 검색
    cur.execute(sql)    #검색 실행
    rs = cur.fetchall()      #모든 자료 가져오기

    for i in rs:
        print(i)
    conn.close()        #db 연결 종료 - 필수


def insert_emp():
    conn = sqlite3.connect("c:/pydb/dbworks/mydb.db")  # db 연결 객체 생성
    cur = conn.cursor()  # db 작업 객체
    sql = "INSERT INTO employee VALUES ('e1002', '손흥민', 30, 50000)" #데이터 추가
    cur.execute(sql)    #검색 실행
    conn.commit()       #커밋 실행 - 필수
    conn.close()

#insert_emp()
select_emp()