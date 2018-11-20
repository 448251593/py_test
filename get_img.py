#import requests;
import os;
import re;
import imghdr;
import time,os,re,urllib,hashlib,sys;

import urllib.request;
#def url_open(url):
#    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#    req = requests.get(url,headers=headers)
#    return req.content;
	
def getHtml(url):
	#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'};			
	req = urllib.request.Request(url = url, headers = headers);
	content =  urllib.request.urlopen(req).read();
	return content;
def  main():
	cat_img = getHtml("http://wx4.sinaimg.cn/mw600/0076BSS5ly1fs3xe3vd00j31kw11x1ky.jpg");
	
	result = imghdr.what('',cat_img);	
	filename='test1.'+result;
	#filename = "test.jpg"
	with open(filename,'wb') as f:
			f.write(cat_img)
			
if __name__ == '__main__':
	main();
