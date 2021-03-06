#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
"""
获取远程图片url demo
opencv_python
numpy
skimage
等包安装
"""
from cv2 import *
import urllib
import numpy as np
import requests as req
from PIL import Image
from io import BytesIO
from skimage import io

img_src = 'http://n1image.hjfile.cn/shetuan/2017-05-17-1495016837-986-732.jpg'
##############
#   opencv   #
##############
#opencv不能直接从网络获取图片，但是opencv的VideoCapture类可以从url加载视频
# cap = VideoCapture(img_src)
# if( cap.isOpened() ):
#     ret, img = cap.read()
#     img = resize(img, (800, 600))
#     imshow("image", img)
#     waitKey(0)

########################
#  opencv+urllib+numpy #
########################
#urllib的urlopen方法返回一个类文件对象，将对象重新编码为图片传给Mat
# resp = urllib.urlopen(img_src)
# image = np.asarray(bytearray(resp.read()), dtype="uint8")
# image = imdecode(image, IMREAD_COLOR)
# image = resize(image, (900, 600))
# imshow("image", image)
# waitKey(0)

########################
#    PIL+requests      #
########################
#字节形式访问请求响应体，用返回的二进制重新创建一张图片

# response = req.get(img_src)
# image = Image.open(BytesIO(response.content))
# image.show()

########################
#    skimage           #
########################
#最方便的方法，直接读物网页图片

image = io.imread(img_src)
io.imshow(image)
io.show()