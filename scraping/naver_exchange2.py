import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)    #url 응답 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')  #html 객체 생성
#ul = soup.find('ul', attrs={'class':'data_lst'})
#print(ul)
lis = soup.select('ul.data_lst li')
#print(lis)

#전체 환률 찾기
for li in lis:
    exchange = li.select_one('span.blind')
    value = li.select_one('span.value')
    #print(exchange.text, ':', value.text)
    print(exchange.string.split(' ')[-1], ':', value.text)
    #공백문자로 구분(split함수)해서 맨 뒤 문자열 추출