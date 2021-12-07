import sqlite3

def getconn():
    con = sqlite3.connect("c:/pydb/mydb.db") #mydb.db가 없으면 생성, 있으면 연결
    return con

def select_emp():
    conn = getconn()
    cur = conn.cursor() #db 작업 객체
    sql = "SELECT * FROM employee"   #db 검색
    cur.execute(sql)    #검색 실행
    rs = cur.fetchall()      #모든 자료 가져오기

    for i in rs:
        print(i)
    conn.close()        #db 연결 종료 - 필수


def insert_emp():
    conn = getconn()
    cur = conn.cursor()  # db 작업 객체
    #입력방법 1 칼럼값을 직접 입력
    #sql = "INSERT INTO employee VALUES ('e1001', '추신수', 40, 40000)" #데이터 추가
    sql = "INSERT INTO employee VALUES (?, ? , ?, ?)"
    cur.execute(sql, ("e1001", '추신수', 40, 40000))    #검색 실행
    conn.commit()       #커밋 실행 - 필수(데이터에 변경이 생겼을때 반드시 명시)
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    # sql = "SELECT emp_id, name FROM employee WHERE salary=50000"
    sql = "SELECT name, salary name FROM employee WHERE emp_id=?"
    cur.execute(sql, ('e1002', )) #튜플 구조는 1개를 명시할 때 콤마 찍어야함
    rs = cur.fetchone()
    print(rs)
    conn.close()

def update_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE employee SET age=? WHERE emp_id=?"
    cur.execute(sql, (33, 'e1004'))
    conn.commit()
    conn.close()

def delete_emp():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE name = ?"
    cur.execute(sql, ('안산', ))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #insert_emp()
    #delete_emp()
    select_emp()
    #select_one()
    #update_emp()