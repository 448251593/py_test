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
reload(sys);
sys.setdefaultencoding( "utf-8" );

def get_page_links(driverweb,page_num):
	
	div_str = '';
	try:
		div_str = driverweb.find_element_by_id('J_mainList').get_attribute('innerHTML')
		#div_str = driverweb.find_element_by_id('J_mainList').get_attribute('innerHTML')
	except:
		print('find J_mainList err');
	
	#with open("J_mainList.html",'wb') as f:
	#	f.write(driverweb.page_source);	
	
	#print(div_str);
	try:
		
		
		str_txt = re.compile(r'<img.+?>').sub('', div_str);
		#print(str_txt);
		urlarr = re.findall(r'<a.*?>.*?</a>',str_txt);
		for  elem in urlarr:
			if elem.find("class=\"title\"") != -1:
				href_url_arr= re.findall(r'href=\".*?\"',elem); 
				href_url = href_url_arr[0][6:len(href_url_arr[0])-1];
				print(href_url);
				href_title_arr =  re.findall(u'>.*?<', elem);
				href_title =  href_title_arr[0][1:len(href_title_arr[0])-1];
				print(href_title);
				
				try:
					get_log_context(driver1,href_url);
				except:
					print('getlog err');

	except:
		print('find links err');


def create_id():
    m = hashlib.md5(str(time.clock()).encode('utf-8'))
    return m.hexdigest()	
#通过url获取网页
def getHtml(url):
	#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}			
	req = urllib2.Request(url = url, headers = headers)
	content = urllib2.urlopen(req).read()
	return content
	
pathfile_current='';
def get_log_context(driver_web,url):

	print ('getting  ' + url)

	pathfile = 'caicai_weixin/'+create_id();	
	print('pathfile='+pathfile)
	pathfile_current = pathfile;
	isExists=os.path.exists(pathfile)
	if isExists:
		print('already exist');
		return 0;
	else:
		#os.system("mkdir -p "+pathfile)
		os.makedirs(pathfile); 

	
	try:
		driver_web.get(url)
		#print (driver_web.page_source)		
		elem = driver_web.find_elements_by_id("img-content")
		print("find img-content")
		
	except:
		print ("find img-content err")
		return -1;


	#with open("source_1.txt",'wb') as f:
	#	f.write(driver_web.page_source)
	
	#try:
	#	driver_web.switch_to.frame(0)
	#	print("switch tblog ok sleep 3")
	#	#time.sleep(3);
	#	time.sleep(10);
	#except:
	#	print("switch_to.frame err")
	#	return -1;


	save_filename = driver_web.title;
	save_filename= re.compile(r' ').sub('', save_filename);
	save_filename= re.compile(r'#').sub('', save_filename);
	

	div_str = ''
	try:
		div_str = driver_web.find_element_by_id('js_content').get_attribute('innerHTML')
	except:
		print ("find js_content  err")
		return -1;
		
	with open("js_content.txt",'wb') as f:
		f.write(div_str);
	try:
		str_txt=div_str
		urlarr = re.findall(r'<img\b.*?data-src=\".*?>',str_txt)
		sortid = 0;
		for  elem in urlarr:			
			tmp_url_arr = re.findall(r'data-src=\".*?\"',elem);
			tmp_url = tmp_url_arr[0].strip()
			tmp_url = tmp_url[len('data-src="'):len(tmp_url)-1]
			print(tmp_url);
			
			file_path_url = get_file_and_save(tmp_url,pathfile,sortid);
			
			tmp_elem = elem.replace(tmp_url,file_path_url);
			tmp_elem = re.compile(r'\ssrc=\".*?\"').sub('',tmp_elem);
			tmp_elem = re.compile(r'data-src').sub('src',tmp_elem);
			
			str_txt = str_txt.replace(elem,tmp_elem);
			print(file_path_url)
			sortid = sortid + 1
		#delete data-src=src <script></script>

		str_txt = re.compile(r'<script(.|\n)*?</script>').sub('',str_txt);
		
		
		str_txt = '<title>'+save_filename+'</title>'+ str_txt
		print('find_element_by_id ok')	
		with open(pathfile+"/"+save_filename+".html",'wb') as f:
			f.write(str_txt);
		print(pathfile+" /page_source.html "+'save ok');
	except:
		print ("loading pic err");
		return -1;
		
	return 0;
	
	
#保存图片
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

	
if __name__ == '__main__':
		
	driver1=webdriver.Firefox();
	driver1.minimize_window();
    #把url整理好按照下面的方式复制多行修改
	get_log_context(driver1,'http://mp.weixin.qq.com/s?__biz=MzA4OTIzMjYzMg==&mid=2652541940&idx=1&sn=15e84a6cbd551375ac7d27fe95010da3&scene=19#wechat_redirect');
	#get_log_context(driver1,'http://mp.weixin.qq.com/s?__biz=MzA4OTIzMjYzMg==&mid=2652541582&idx=1&sn=17c3e94d2956760f17a6862ede2dc5c6&scene=19#wechat_redirect');
	#get_log_context(driver1,'http://mp.weixin.qq.com/s?__biz=MzA4OTIzMjYzMg==&mid=2652541582&idx=2&sn=a4ecf38a29040c35a56b72f782ac3aac&scene=19#wechat_redirect');
	#get_log_context(driver1,'http://mp.weixin.qq.com/s?__biz=MzA4OTIzMjYzMg==&mid=2652541582&idx=3&sn=9259f0eb146fcba4406a4c0e26035ee4&scene=19#wechat_redirect');

	

	driver1.quit();
