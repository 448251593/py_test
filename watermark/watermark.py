#-*- coding:utf-8 -*-
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#������ʹ�õ�����
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)

#��ͼƬ
imageFile = "004.jpeg"
im1 = Image.open(imageFile)

#��ͼ
markstr="QQ:448251593"
draw = ImageDraw.Draw(im1)
draw.text((im1.size[0]-len(markstr)*14, im1.size[1]-23), markstr, (255, 0, 0), font=font)    #��������λ��/����/��ɫ/����
draw = ImageDraw.Draw(im1)                          #Just draw it!
print(im1.size[0]-1)
#���ͼƬ
im1.save("target.jpg")