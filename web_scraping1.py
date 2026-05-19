from bs4 import BeautifulSoup
import re

html_doc="""
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
    <div data-role="page" data-last-modified="2022-01-01" data-foo="value">This is a div with data attributes.</div>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2" data-info="more info">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3" data-info="even more info">Tillie abcd</a>
    ; and they lived at the bottom of a well.</p>
    <p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc,'html_parser')
print(soup.prettify) 

# <title> 태그 접근
print(soup.title)  # <title>The Dormouse's story</title>

# <title> 태그의 이름
print(soup.title.name)  # 'title'

# <title> 태그의 텍스트 내용
print(soup.title.string)  # 'The Dormouse's story'

# <title> 태그의 부모 태그 이름
print(soup.title.parent.name)  # 'head'

# 첫 번째 <p> 태그 접근
print(soup.p)  # <p class="title"><b>The Dormouse's story</b></p>

# <p> 태그의 클래스 속성 값
print(soup.p['class'])  # ['title']

# 첫 번째 <a> 태그 접근
print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# 모든 <a> 태그를 찾아 리스트로 반환
print(soup.find_all('a'))
# 출력: 모든 <a> 태그 리스트

# id가 "link3"인 <a> 태그 찾기
print(soup.find(id="link3"))  # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

#정규표현식 태그 찾기
print(soup.find_all(string=re.complie('sister')))

#CSS 컬렉터
print(soup.select('p.sister'))
print(soup.select('a[herf]'))