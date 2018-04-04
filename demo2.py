#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
from selenium import webdriver
import time
from PIL import Image
from io import StringIO
import urllib.request
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://unsplash.com')
#assert 'Free' in browser.title
# browser.execute_script("window.scrollBy(0,300000)")
# time.sleep(5)
for i in range(1,5):

    yheight=i*3000
    browser.execute_script("window.scrollBy(0,3000)")
    time.sleep(5)

# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
# print(browser.page_source)
# textElement=browser.find_element_by_id('app')
# img=browser.find_element_by_class_name('_3vgBX')
# print(img)
print(11)
# utype=browser.find_elements_by_class_name('_2zEKz')
# print(type(utype))
img=[]
for link in browser.find_elements_by_class_name('_2zEKz'):
#    print(link.get_attribute("src"))
    img.append(link.get_attribute("src"))
    # print(img[0])
    # file=StringIO(urllib.request.urlopen(img[0]).read())
    # im = Image.open(file)
    # print(im)

print(img)
print(len(img))
# print(textElement)
browser.quit()