from bs4 import BeautifulSoup

html_str = """
<html>
  <body>
    <ul class='item'>
        <li>인공지능</li>
        <li>빅데이터</li>
        <li>로봇공학</li>
    </ul>
    <ul class="lang">
        <li>Python</li>
        <li>Java</li>
        <li>C#</li>
    </ul>
  </body>
</html>
"""

soup = BeautifulSoup(html_str, "html.parser")
first_ul = soup.find('ul', attrs={'class':'item'})
all_li = first_ul.find_all('li')    #find_all() : 찾은 값 list로 반환
print(all_li)
print(all_li[1])
print(all_li[1].text)