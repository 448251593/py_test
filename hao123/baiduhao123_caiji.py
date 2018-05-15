#coding:utf-8
from selenium import webdriver
import time,os,re,urllib,urllib2,hashlib,sys

import imghdr;
#import xlrd,xlwt
#from xlutils.copy import copy
#使用selenium
#使用selenium的隐藏PhantimJS浏览器登陆账号后对内容获�?#注意frame与iframe的格式框切换
#driver = webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
#driver=webdriver.Chrome()

#driver=webdriver.PhantomJS()
#driver.set_preference('network.proxy.type', 1)
#driver.set_preference('network.proxy.http', '127.0.0.1')
#driver.set_preference('network.proxy.http_port', 17890)
#driver.maximize_window() 


driver1=webdriver.Firefox();
driver1.minimize_window();

#driver=webdriver.Firefox()
#driver.minimize_window() 
reload(sys)
sys.setdefaultencoding( "utf-8" );


def create_id():
    m = hashlib.md5(str(time.clock()).encode('utf-8'))
    return m.hexdigest()	
#通过url获取图片内容
def getHtml(url):
	#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}			
	req = urllib2.Request(url = url, headers = headers)
	content = urllib2.urlopen(req).read()
	return content
	
pathfile_current='';
#获取网页内容自动下载图片
def get_log_context(driver_web,url):

	print ('getting  ' + url)
	#检查路径
	pathfile = create_path_base_url(url)
	if len(pathfile)==0:
		print("get path from url err")
		return 0;
	pathfile = 'haomeizi/'+pathfile	
	print('pathfile='+pathfile)
	pathfile_current = pathfile;
	isExists=os.path.exists(pathfile)
	if isExists:
		print('already exist');
		return 0;
	else:
		#os.system("mkdir -p "+pathfile)
		os.makedirs(pathfile); #创建目录
	#查找相关html节点
	try:
		driver_web.get(url)
		#print (driver_web.page_source)		
		
		elem = driver_web.find_elements_by_id("J_article")
		print("find J_article")
		
	except:
		print ("find J_article err")
		return -1;



	#获取网页标题
	save_filename = driver_web.title;
	save_filename= re.compile(r' ').sub('', save_filename);
	save_filename= re.compile(r'#').sub('', save_filename);
	


	div_str = ''
	try:#获取节点的html
		div_str = driver_web.find_element_by_id('J_article').get_attribute('innerHTML')
	except:
		print ("find J_article  err")
		return -1;
	#保存html,一般用于调试	
	with open("J_article_src.txt",'wb') as f:
		f.write(div_str);
		
	try:
		str_txt=div_str
		urlarr = re.findall(r'<img\b.*?src=\".*?>',str_txt)#正则提取图片url
		sortid = 0;
		for  elem in urlarr:			
			tmp_url_arr = re.findall(r'\simg-src=\".*?\"',elem);#二级提取真正的图片url
			tmp_url = tmp_url_arr[0].strip()
			tmp_url = tmp_url[len('img-src="'):len(tmp_url)-1]
			print(tmp_url);#打印输入url
			#获取并保存图片文件
			file_path_url = get_file_and_save(tmp_url,pathfile,sortid)
			str_txt = str_txt.replace(tmp_url,file_path_url)#在本地的网页html替换图片url,指向本地路径
			print(file_path_url)
			sortid = sortid + 1
		#delete data-src=src <script></script>
		#用正则匹配并清除没有用的一些网址
		strinfo = re.compile(r'\ssrc=\"https://gss0.*?\"')
		str_txt = strinfo.sub('', str_txt)
		strinfo = re.compile(r'\swap_url=\".*?\"')
		str_txt = strinfo.sub('', str_txt)
		
		strinfo = re.compile(r'\simg-src=')
		str_txt = strinfo.sub(' src=', str_txt)
		#保存html 到本地
		str_txt = '<title>'+save_filename+'</title>'+str_txt
		print('find_element_by_id ok')	
		with open(pathfile+"/"+save_filename+".html",'wb') as f:
			f.write(str_txt);
		print(pathfile+" /page_source.html "+'save ok');
	except:
		print ("loading pic err");
		return -1;
		
	return 0;
	
	
	
def get_file_and_save(url, path,sortid):
	cat_img = getHtml(url)
	print ("down load ok")

	result = imghdr.what('',cat_img);
	
	filename=str(sortid).zfill(3)+'_'+create_id()+'.'+result
	
	pathfilename=path+"/"+filename
	
	with open(pathfilename,'wb') as f:
		f.write(cat_img)
		print("save pic ok, "+pathfilename)	
	return filename
	
	

def create_path_base_url(url):
	strid = re.findall(r'/haomeizi/[0-9]*',url)#haomeizi/1109
	path = strid[0][10:len(strid[0])]
	return path


file_errlog="hao123_caijilog.log";
def err_log(log_data):
	with open('haomeizi/'+file_errlog,'a') as f:
		f.write(log_data+'\n')	
	
def debug_test():
	pathfile = create_path_base_url('https://user.qzone.qq.com/822989010/blog/1488525103')
	if len(pathfile)==0:
		print("get path from url err")
		return
	pathfile = './'+pathfile	
	print('pathfile='+pathfile)
	
	
	with open("page_source_2.html",'r') as f:
		str_txt=f.read()
		#urlarr = re.findall(r'data-src=".*?"',str_txt)
		urlarr = re.findall(r'<img\b.*?data-src=".*?>',str_txt)
		for  elem in urlarr:			
			tmp_url = elem[len('data-src=')+1:len(elem)-1]
			#file_path_url = get_file_and_save(tmp_url,pathfile)
			#print(file_path_url)
			#str_txt = str_txt.replace(tmp_url,file_path_url)
			print(tmp_url)
			
		try:
			with open(pathfile+"/page_source_31.html",'wb') as f:
				f.write(str_txt)
		except:
			print('save err')
	
			
			
if __name__ == '__main__':
	
	#网址修改后即可
	get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1114');
	time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1113');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1112');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1111');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1110');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1109');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1108');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1107');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1106');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1105');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1104');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1103');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1102');
	#time.sleep(3);
	#get_log_context(driver1,'http://www.hao123.com/gaoxiao/haomeizi/1101');
	#time.sleep(3);
	#debug_test()	

	driver1.quit();

	#driver.quit();
