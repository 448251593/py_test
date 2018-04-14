#-*- coding:utf-8 -*-
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#设置所使用的字体
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)

#打开图片
imageFile = "004.jpeg"
im1 = Image.open(imageFile)

#画图
markstr="QQ:448251593"
draw = ImageDraw.Draw(im1)
draw.text((im1.size[0]-len(markstr)*14, im1.size[1]-23), markstr, (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
draw = ImageDraw.Draw(im1)                          #Just draw it!
print(im1.size[0]-1)
#另存图片
im1.save("target.jpg")