import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

div = soup.find('div', attrs={'class': 'service_area'})
first_a = div.find('a')
#print(first_a)
#print(first_a.text)

#쥬니어 네이버 문자열 찾기
all_a = div.find_all('a')
#print(all_a)
print(all_a[1].text)