#기본 매개변수 - 매개 변수를 초기화하여 선언
#함수 호출시 생략하면 기본값으로 출력

def print_string(text, count=1):
    for i in range(count):      #range(0, 3) 인데 0은 생략 가능
        print(text)



print_string("Hello~")  #count 생략 호출 - 무조건 기본값(선언시 지정한 숫자)
print_string("Hello~", 4)   #count 지정시 무조건 지정된 수 우선