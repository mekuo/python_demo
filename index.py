#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
import requests

# print('hell');
r = requests.get('https://unsplash.com') #像目标url地址发送get请求，返回一个response对象
# print(r.text);#text是http response的网页HTML
# str='12344';

# def demo(self):
#     print('this is demo ' + self)
#
# demo('123');

from bs4 import BeautifulSoup
import bs4
# html_doc = """
# <html><head><title>网页标题是什么自己定义</title></head>
# <body>
# <P><!--zhe--></p>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """

html_doc=r.text
soup = BeautifulSoup(html_doc, 'lxml')


# print(soup.p)
#
# #对标签的直接子节点进行循环
# for child in soup.body.children:
#     print(child)
str=123
print(str)

# print(soup.prettify())

# print(soup.title.string)
#
# for link in soup.find_all('a'):
#     print(link.get('href'))
# p=soup.find('p');
# print(p.string);
#
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup,'lxml')
comment = soup.b.string
# print(type(comment))
# print(comment)
#
is_ok='yes'
if type(comment) == bs4.element.Comment:
    print(is_ok)
else:
    print('no')

str