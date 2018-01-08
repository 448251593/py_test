#coding:utf-8
from selenium import webdriver
import time,os,re,urllib,urllib2,hashlib,sys

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
#通过url获取网页
def getHtml(url):
	#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}			
	req = urllib2.Request(url = url, headers = headers)
	content = urllib2.urlopen(req).read()
	return content
	
pathfile_current='';
def get_log_context(driver_web,url,str_title,page_num):

	print ('getting  ' + url)
	pathfile = create_path_base_url(url)
	if len(pathfile)==0:
		print("get path from url err")
		return 0;
	pathfile = 'blog/page'+page_num+'/'+pathfile	
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
		
		elem = driver_web.find_elements_by_id("tblog")
		print("find tblog")
		
	except:
		print ("get_log_context err")
		return -1;


	#with open("source_1.txt",'wb') as f:
	#	f.write(driver_web.page_source)
	
	try:
		driver_web.switch_to.frame(0)
		print("switch tblog ok sleep 3")
		#time.sleep(3);
		time.sleep(10);
	except:
		print("switch_to.frame err")
		return -1;


	#save_filename = str_title 
	try:
		#elem = driver_web.find_elements_by_xpath("//*[@class=blog_tit_detail]")
		elem = driver_web.find_element_by_class_name("blog_tit_detail")
		save_filename = elem.get_attribute('textContent')
		save_filename = save_filename.strip()
		print('title='+save_filename)
	except:
		print('find_elements_by_xpath blog_tit_detail err')
		return -1;

		
	#with open("source_2.txt",'wb') as f:

	#	f.write(driver_web.page_source)

	div_str = ''
	try:
		div_str = driver_web.find_element_by_id('blogDetailDiv').get_attribute('innerHTML')
	except:
		print ("find blogDetailDiv  err")
		return -1;
	
	try:
		str_txt=div_str
		urlarr = re.findall(r'<img\b.*?data-src=\".*?>',str_txt)
		sortid = 0;
		for  elem in urlarr:			
			tmp_url_arr = re.findall(r'\ssrc=\".*?\"',elem);
			tmp_url = tmp_url_arr[0].strip()
			tmp_url = tmp_url[len('src="'):len(tmp_url)-1]
			print(tmp_url);
			
			file_path_url = get_file_and_save(tmp_url,pathfile,sortid)
			str_txt = str_txt.replace(tmp_url,file_path_url)
			print(file_path_url)
			sortid = sortid + 1
		#delete data-src=src <script></script>
		strinfo = re.compile(r'data-src=\".*?\"')
		str_txt = strinfo.sub('', str_txt)
		strinfo = re.compile(r'<script(.|\n)*?</script>')
		str_txt = strinfo.sub('', str_txt)
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

	
	filename=str(sortid).zfill(2)+'_'+create_id()+'.jpg'
	pathfilename=path+"/"+filename
	
	with open(pathfilename,'wb') as f:
		f.write(cat_img)
		print("save pic ok,"+pathfilename)	
	return filename
	
	

def create_path_base_url(url):
	strid = re.findall(r'/blog/[0-9]*',url)
	path = strid[0][6:len(strid[0])]
	return path


file_errlog="log_caijiqqlog.log";
def err_log(log_data):
	with open('./blog/'+file_errlog,'a') as f:
		f.write(log_data+'\n')	
	
def retry_url():
	with open("./blog/log_caijiqqlog.log",'r') as f:
		str_txt=f.read()
		#print(str_txt);
		str_arr = str_txt.split('\n');
		print(len(str_arr));
		for i in range(0,len(str_arr)-1) :
			elem = str_arr[i];
			
			pagenum_arr = re.findall(r'page=.*,',elem)
			url_arr = re.findall(r'http.*',elem)
			
			page_t = pagenum_arr[0][5:len(pagenum_arr[0])-1];
			print(page_t);			
			print(url_arr[0]);			
			#get_log_context(driver1,url_arr[0],'title no used', page_t);
			
if __name__ == '__main__':

	#print('start...');
	#get_log_context(driver1,'http://user.qzone.qq.com/822989010/blog/1486607534','test','2')
	#debug_test()	
	retry_url();
	driver1.quit();

	#driver.quit();
