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

def get_page_links(driverweb,page_num):
	#try:
	#	if page_num!='1':
	#		print('get page='+page_num+' data');
	#		driverweb.find_element_by_xpath("//input[starts-with(@id,'pageIndex_input')]").click()
	#		print ('1')
	#		driverweb.find_element_by_xpath("//input[starts-with(@id,'pageIndex_input')]").clear()
	#		print ('2')
	#		driverweb.find_element_by_xpath("//input[starts-with(@id,'pageIndex_input')]").send_keys(page_num)
	#		print ('3')
	#		driverweb.find_element_by_xpath("//button[@type='button']").click()
	#		print ('4')
	#		print('sleep 5')
	#except:
	#	print('go to page err');
	#	return;
	#time.sleep(3);
	
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
		#Links = driverweb.find_elements_by_xpath("//a[starts-with(@href,'http://user.qzone.qq.com/822989010/blog/')]");
		#count1 = 0;
		#total = 0;
		#for link in Links:
		#	url_context= link.get_attribute('href');
		#	print (url_context);
		#	total=total+1;
			#str_title = link.get_attribute('innerHTML');
			#str_title = str_title.strip();
			#str_title = str_title.replace('<span>','');
			#str_title = str_title.replace('</span>','');
			#print(str_title);
		#for link in Links:
		#	url_context= link.get_attribute('href');
		#	
		#	count1=count1+1
		#	print('progress=('+str(count1)+'/'+str(total)+')')
		#	
		#	str_title = link.get_attribute('innerHTML');
		#	str_title = str_title.strip();
		#	str_title = str_title.replace('<span>','');
		#	str_title = str_title.replace('</span>','');
		#	
		#	#pathfile = create_path_base_url(url);
		#	try:
		#		rslt = get_log_context(driver1,url_context,str_title,page_num);
		#		if rslt == -1:
		#			err_log('page='+page_num+','+url_context);					
		#			os.system("rm "+pathfile_current+' -rf');
		#	except:
		#		err_log('page='+page_num+','+url_context);
		#		os.system("rm "+pathfile_current+' -rf');


	except:
		print('find links err');

def driver_browser_init(driverweb):
	rstl = 0
	#url = 'http://www.hao123.com/gaoxiao/haomeizi/list';
	url = 'file:///D:/py_test/hao123/J_mainList.html'
	try:
		driverweb.get(url);	
		print("get  "+url+'  ok' );
	except:
		print('get url err');
		rstl = -1;

	time.sleep(10);
	#with open("source_frame.html",'wb') as f:
	#	f.write(driverweb.page_source);
	return 0;

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
	#pathfile = create_path_base_url(url)
	#if len(pathfile)==0:
	#	print("get path from url err")
	#	return 0;
	pathfile = 'hao123gaoxiao/'	
	print('pathfile='+pathfile)
	pathfile_current = pathfile;
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
		
	except:
		print ("find J_article err")
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
	#save_filename= save_filename.replace('hao123');
	#save_filename= save_filename.replace('上网导航');
	
	print("save_filename="+save_filename);

	

		
	#with open("source_2.txt",'wb') as f:
	#	f.write(driver_web.page_source)
	#div_str = ''
	#try:
	#	div_str = driver_web.find_element_by_class_name('brief').get_attribute('innerHTML')
	#	print ("find brief ")
    #
	#except:
	#	print ("find brief  err")
	#	return -1;
	#	
	#try:
	#	titlearr = re.findall(r'title=\".*?\"',div_str)
	#	for  elem in titlearr:
	#		save_filename = elem[0][len("title=\"")-2];
	#		print("title->"+save_filename);
	#		break;
	#except:
	#	print("title err");

	try:
		div_str = driver_web.find_element_by_class_name('pic-content').get_attribute('innerHTML')
		print ("find pic-content ")
	except:
		print ("find pic-content  err")
		return -1;
		
	#  <div class="brief">([\s\S]*?)</div>
	# <div class="pic-content">([\s\S]*?)</div>

	with open("J_article_src.txt",'wb') as f:
		f.write(div_str);
		
	str_txt=div_str
	
	picurl_str = "";
	try:
		urlarr = re.findall(r'src=\".*? ',str_txt)
		for  elem in urlarr:	
			picurl_str		= urlarr[0][len('src="'):len(urlarr[0])-2];
			print("pic-----------------------"+picurl_str)
			get_file_and_save(picurl_str,pathfile,0, save_filename)			#save_filename[0:len(save_filename)-14]
			break;
	except:
		print("pic url find err")
	
	
		

	
	#try:
	#	str_txt=div_str
	#	urlarr = re.findall(r'<img\b.*?src=\".*?>',str_txt)
	#	sortid = 0;
	#	for  elem in urlarr:			
	#		tmp_url_arr = re.findall(r'\simg-src=\".*?\"',elem);
	#		tmp_url = tmp_url_arr[0].strip()
	#		tmp_url = tmp_url[len('img-src="'):len(tmp_url)-1]
	#		print(tmp_url);
	#		
	#		file_path_url = get_file_and_save(tmp_url,pathfile,sortid)
	#		str_txt = str_txt.replace(tmp_url,file_path_url)
	#		print(file_path_url)
	#		sortid = sortid + 1
	#	#delete data-src=src <script></script>
	#	strinfo = re.compile(r'\ssrc=\"https://gss0.*?\"')
	#	str_txt = strinfo.sub('', str_txt)
	#	strinfo = re.compile(r'\swap_url=\".*?\"')
	#	str_txt = strinfo.sub('', str_txt)
	#	
	#	strinfo = re.compile(r'\simg-src=')
	#	str_txt = strinfo.sub(' src=', str_txt)
	#	
	#	str_txt = '<title>'+save_filename+'</title>'+str_txt
	#	print('find_element_by_id ok')	
	#	with open(pathfile+"/"+save_filename+".html",'wb') as f:
	#		f.write(str_txt);
	#	print(pathfile+" /page_source.html "+'save ok');
	#except:
	#	print ("loading pic err");
	#	return -1;
	#	
	return 0;
	
	
	
def get_file_and_save(url, path,sortid, title):
	cat_img = getHtml(url)
	print ("down load ok")

	result = imghdr.what('',cat_img);
	
	filename=str(sortid).zfill(3)+'_'+title+'.'+result
	
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
	#pathfile = create_path_base_url('https://user.qzone.qq.com/822989010/blog/1488525103')
	#if len(pathfile)==0:
	#	print("get path from url err")
	#	return
	#pathfile = './'+pathfile	
	#print('pathfile='+pathfile)
	
	
	with open("J_article_src.txt",'r') as f:
		str_txt=f.read()
		#print(str_txt);
		#urlarr = re.findall(r'data-src=".*?"',str_txt)
		urlarr = re.findall(r'brief([\s\S]*?)</div>',str_txt)
		for  elem in urlarr:			
			#tmp_url = elem[len('data-src=')+1:len(elem)-1]
			#file_path_url = get_file_and_save(tmp_url,pathfile)
			#print(file_path_url)
			#str_txt = str_txt.replace(tmp_url,file_path_url)
			print("-----------------------");
			title_urlarr = re.findall(r'title=\".*?>',elem);
			print(title_urlarr[0])
			print("-----------------------");
			
		urlarr = re.findall(r'pic-content([\s\S]*?)</div>',str_txt)
		for  elem in urlarr:			
			#tmp_url = elem[len('data-src=')+1:len(elem)-1]
			#file_path_url = get_file_and_save(tmp_url,pathfile)
			#print(file_path_url)
			#str_txt = str_txt.replace(tmp_url,file_path_url)
			print("-----------------------");
			
			pic_urlarr = re.findall(r'src=\".*? ',elem);
			print(pic_urlarr[0])
			print("-----------------------");
			break;
		#try:
		#	with open(pathfile+"/page_source_31.html",'wb') as f:
		#		f.write(str_txt)
		#except:
		#	print('save err')
	
			
			
if __name__ == '__main__':

	#debug_test();
	get_log_context(driver1,'http://www.hao123.com/gaoxiao/detail/388655');
	#time.sleep(3);


	driver1.quit();

	#driver.quit();
