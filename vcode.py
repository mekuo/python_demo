#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
import pytesseract

from PIL import Image

png= "D:\\timg2.jpg"
print('开始处理')
image = Image.open(png)
print(image)
enhancer = ImageEnhance.Color(image)
enhancer = enhancer.enhance(0)
enhancer = ImageEnhance.Brightness(enhancer)
enhancer = enhancer.enhance(2)
enhancer = ImageEnhance.Contrast(enhancer)
enhancer = enhancer.enhance(8)
enhancer = ImageEnhance.Sharpness(enhancer)
im = enhancer.enhance(20)
print (pytesseract.image_to_string(im))
vcode = pytesseract.image_to_string(image,lang = 'chi_sim')

print ('---'+vcode)