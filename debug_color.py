# from PIL import ImageColor
# print(ImageColor.getcolor('red', 'RGBA'))
# # 也可以只以RBG的方式查看
# print(ImageColor.getcolor('black', 'RGB'))

from PIL import Image

im_path = r'D:\PIL_rabbit_copy.jpg'
im = Image.open(im_path)
width, height = im.size
# 宽高
print(im.size, width, height)
# 格式，以及格式的详细描述
print(im.format, im.format_description)

im.save(r'C:\Users\111\Desktop\rabbit_copy.jpg')
im.show()