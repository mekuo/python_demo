#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
"""
@ Author：mekuo 获取远程地址url
"""
from PIL import Image
from io import BytesIO
import requests
import urllib.request

url='https://images.unsplash.com/photo-1442508748335-fde9c3f58fd9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=efb6133a444ebb07753d8fa38eb6d2f6&w=1000&q=80'
content=urllib.request.urlopen(url).read()
#content.decode()

c=str(content)
print(c)
print(type(c))
response = requests.get(url)
image = Image.open(BytesIO(response.content))
image.show()

