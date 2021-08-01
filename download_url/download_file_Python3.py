#coding:utf-8
# -*- coding: UTF-8 -*-
import time,os,re,urllib,hashlib,sys;
import sqlite3;
import imghdr;
import urllib.request;








	
#通过url获取图片
def getHtml(url):
	#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'};			
	req = urllib.request.Request(url = url, headers = headers);
	content =  urllib.request.urlopen(req).read();
	return content;
	
pathfile = 'MEIZITU/';
def init_get(driver_web,url):
	print ('getting  ' + url)
	#pathfile = create_path_base_url(url)
	#if len(pathfile)==0:
	#	print("get path from url err")
	#	return 0;
	print('pathfile='+pathfile)
	isExists=os.path.exists(pathfile)
	if isExists:
		print('already exist');
		#return 0;
	else:
		#os.system("mkdir -p "+pathfile)
		os.makedirs(pathfile); 
	
	try:
		driver_web.get(url)
		#print (driver_web.page_source)		
		
		#elem = driver_web.find_elements_by_id("J_article")
		#print("find J_article")
		return 0;
	except:
		print ("find J_article err")
		return -1;
#获取网页内容并提取图片保存		
def get_log_context(picurl_str, count):



	#获取保存图片
	try:
		print("picurl_str=" + picurl_str);
		get_file_and_save(picurl_str,  count);
	except:
		print("get_file_and_save err");

		
	return 2;
	

	
def get_file_and_save(url,  sortid):
	cat_img = getHtml(url)
	print ("down load ok")

		
	pathfilename= str(sortid).zfill(3) + ".ts"
	
	with open(pathfilename,'wb') as f:
		f.write(cat_img)
		print("save pic ok, "+pathfilename)	
	return pathfilename


#---------------------------运行主函数------------------------------
def exe_main(url_addr, startid , endid):

	tmp_ct = startid;
	#000.ts
	
	
	url_suffix = ".ts"
	print(url_addr[0:-5]);

	while(tmp_ct <= endid):
		ret2 = get_log_context(url_addr[0:-5] + str(tmp_ct).zfill(3) + url_suffix,tmp_ct);#获取当前网页的图片
		if ret2 == 2:
			# time.sleep(1);
			print("ok")
		else:
			print("err break=" + str(ret2));
			#break;
		tmp_ct = tmp_ct + 1;
	os.system("copy /b *.ts all.ts");
	

if __name__ == '__main__':
	#根据m3u8文件信息填充现在文件的间隔
	url_addr = "https://m001.m1m2m3u8mp4.com/F0604/yrza/yrza.m3u8"
	exe_main(url_addr,000, 2);

