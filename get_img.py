import requests;
import os;
import re;
import imghdr;

def url_open(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    req = requests.get(url,headers=headers)
    return req.content;

def  main():
	cat_img = url_open("https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3332982453,1637075014&fm=27&gp=0.jpg");
	
	result = imghdr.what('',cat_img);	
	filename='test1.'+result;
	#filename = "test.jpg"
	with open(filename,'wb') as f:
			f.write(cat_img)
			
if __name__ == '__main__':
	main();
