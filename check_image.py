from selenium import webdriver
import time,os,re,urllib,urllib2,hashlib,sys
from PIL import Image;
import imghdr;
def check_pic_type(filename):
	#img = Image.open(filename)
	#print(img.format)  # 'JPEG'
	result = imghdr.what(filename);
	print(result);
	
def create_id():
    m = hashlib.md5(str(time.clock()).encode('utf-8'))
    return m.hexdigest();
def getHtml(url):
	#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}			
	req = urllib2.Request(url = url, headers = headers)
	content = urllib2.urlopen(req).read()
	return content
	
def get_file_and_save(url, path,sortid):
	cat_img = getHtml(url)
	print ("down load ok")

	#with open('pic.data','wb') as f:
	#	f.write(cat_img)
		
	result = imghdr.what('',cat_img);
	
	filename=str(sortid).zfill(3)+'_'+create_id()+'.'+result
	pathfilename=filename
	
	with open(pathfilename,'wb') as f:
		f.write(cat_img)
		print("save pic ok,"+pathfilename)	
	return filename
	
if __name__ == '__main__':
	#check_pic_type('test.jpg');
	get_file_and_save('http://sc1.hao123img.com/erjiImg//haomeizi/36580689c9e09714d3ce02ecc118e897','pictype',1);