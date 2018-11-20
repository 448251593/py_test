#coding:utf-8
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time,os,re,urllib,hashlib,sys;
import sqlite3;
import imghdr;
import urllib.request;
#import xlrd,xlwt
#from xlutils.copy import copy
#使用selenium
#使用selenium的隐藏PhantimJS浏览器登陆账号后对内容获??#注意frame与iframe的格式框切换
#driver = webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
#driver=webdriver.Chrome()

#driver=webdriver.PhantomJS()
#driver.set_preference('network.proxy.type', 1)
#driver.set_preference('network.proxy.http', '127.0.0.1')
#driver.set_preference('network.proxy.http_port', 17890)
#driver.maximize_window() 


#reload(sys)
#sys.setdefaultencoding( "utf-8" );
	
def sqlite3_con():
	conn = sqlite3.connect('pic_info.db')
	print ("Opened database successfully");
	c = conn.cursor()
	try:
		c.execute("CREATE TABLE pic_info  (MD5_PIC        TEXT      NOT NULL);")
		conn.commit()
		print ("Table created successfully");
	except:
		print ("Table exist");
	
	return conn;
	
conn=sqlite3_con();



def create_id():
    m = hashlib.md5(str(time.clock()).encode('utf-8'))
    return m.hexdigest();
	
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
def get_log_context(driver_web, count):

	#
	with open("current_url.txt",'w') as f:
		f.write(driver_web.current_url);
	div_str = ''
	try:
		div_str = driver_web.find_element_by_class_name('commentlist').get_attribute('innerHTML')
		#print ("find commentlist ok "+div_str);
		print ("find commentlist ok ");
	except:
		print ("find brief  err");
	
	
	try:
		urlarr = re.findall(r'<img\b.*?src=\".*?>',div_str);
		for  elem in urlarr:
			print('getting pic url='+elem);
			
		for  elem in urlarr:
			urlpic = re.findall(r'http[\s\S]*?\"',elem);
			if len(urlpic) > 0:
				picurl_str = urlpic[0][0:len(urlpic[0])-1];
				print('getting pic url='+picurl_str);
				#获取保存图片
				try:
					get_file_and_save(picurl_str, pathfile, count);
				except:
					print("get_file_and_save err");
			else:
				print("no find url");

	except:
		print ("getting  pic err");
		
	return 2;
	
	
#点击下一页函数
def  get_next_click(driver,count):
	try:
		#selenium 定位下一页的按钮并点击,此地方需要根据网站的变化进行调试,
		#driver.find_element_by_xpath("//div[@class='cp-pagenavi']/a[6]").click();
		#driver.find_element_by_xpath("//div[@id='comments']/div[2]/div/a[5]").click();
		driver.find_element_by_xpath("//a[@class='previous-comment-page']").click()
		print("next click ok ct="+str(count));
	except:
		print("next click err ct="+str(count));
		return -1;
	
def get_file_and_save(url, path, sortid):
	cat_img = getHtml(url)
	print ("down load ok")

	md5obj = hashlib.md5();
	md5obj.update(cat_img);
	hash = md5obj.hexdigest();
	print(hash);
	
	ret = insert_pic_info(conn, hash)
	if ret == 1:
		result = imghdr.what('',cat_img);
		
		filename=str(sortid).zfill(3)+'_'+hash+'.'+result
		
		pathfilename=path+filename
		
		with open(pathfilename,'wb') as f:
			f.write(cat_img)
			print("save pic ok, "+pathfilename)	
		return filename
	else:
		print ("pic already exist");
		return ""

#---------------------------运行主函数------------------------------
def exe_main(count):

	#浏览器驱动变量,控制浏览器的
	driver1=webdriver.Firefox();
	driver1.minimize_window();	
	with open("current_url.txt",'r') as f:
		str_txt=f.read()
	if (len(str_txt) ==0):
		print("start url is null");
		return ;
	ret = init_get(driver1,str_txt);
	

	tmp_ct = 0;

	
	if ret==0:
		
		while(tmp_ct < count):
			tmp_ct = tmp_ct + 1;
			ret2 = get_log_context(driver1,tmp_ct);#获取当前网页的图片
			if ret2 == 2:
				time.sleep(2);
				get_next_click(driver1,tmp_ct);#点击下一页
				time.sleep(3);#点击完成延时等待网页
			else:
				print("err break=" + str(ret2));
				#break;
	else:
		print("init_get err");
	driver1.quit();

def insert_pic_info(cnn_hd, md5):
	#select 是否存在,不存在则插入
	flag = 0;
	c = cnn_hd.cursor()
	#c.execute("insert into pic_info values('"+md5+"')");
	#return;
	sql_select =  "select MD5_PIC from pic_info where MD5_PIC='"+md5+"';";
	print(sql_select)
	cursor =  c.execute(sql_select);	
	rslt = len(cursor.fetchall());
	print("count ="+str(rslt));
	
	if rslt == 0:
		print("no item,can insert");
		c.execute("insert into pic_info values('"+md5+"')");
		print("insert sucess");	
		flag = 1;
	else:
		print(md5+" is exist");
		flag = 0;
	cnn_hd.commit()
	return flag;	
if __name__ == '__main__':
	#输入一次采集的数量300
	exe_main(6);

