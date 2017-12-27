#coding:utf-8
from selenium import webdriver
import time,os,re,urllib,urllib2,hashlib,sys

#import xlrd,xlwt
#from xlutils.copy import copy

#driver = webdriver.PhantomJS(executable_path="E:\\mac\\id\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
#driver=webdriver.Chrome()

#driver=webdriver.PhantomJS()
#driver.set_preference('network.proxy.type', 1)
#driver.set_preference('network.proxy.http', '127.0.0.1')
#driver.set_preference('network.proxy.http_port', 17890)
#driver.maximize_window() 
driver=webdriver.Firefox()
driver.minimize_window() 
reload(sys)
sys.setdefaultencoding( "utf-8" )
def get_page_links(page_num):		
	driver.find_element_by_xpath("//input[starts-with(@id,'pageIndex_input')]").click()
	print ('1')
	driver.find_element_by_xpath("//input[starts-with(@id,'pageIndex_input')]").clear()
	print ('2')
	driver.find_element_by_xpath("//input[starts-with(@id,'pageIndex_input')]").send_keys(page_num)
	print ('3')
	driver.find_element_by_xpath("//button[@type='button']").click()
	print ('4')
	print('sleep 5')
	time.sleep(5);
	
	with open("page_source_frame_new.html",'wb') as f:
		f.write(driver.page_source);
	try:
		Links = driver.find_elements_by_xpath("//a[starts-with(@href,'http://user.qzone.qq.com/822989010/blog/')]");
		for link in Links:
			print (link.get_attribute('href'));
			#get_log_context('https://user.qzone.qq.com/822989010/blog/1488525155');
			#print (elem.get_attribute("title"));
	except:
		print('find links err')
		
def driver_browser_init():
	url = 'https://user.qzone.qq.com/822989010/2';
	#url = 'file:///home/bcg/samba/test/selenium/page_source_frame.html'
	try:
		driver.get(url);	
		print("get  "+url+'  ok' );
		return 0;
	except:
		print('get url err');
		return -1;
		
	try:
		driver.switch_to.frame(0);
		
		print('switch frame 0 ok,sleep 10');
		time.sleep(10);
		return 0;
	except:
		print('switch frame 0 err');
		return -1;
	
	with open("page_source_frame.html",'wb') as f:
		f.write(driver.page_source);
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
	
	#work_path='E:\\0930\\WWWW.csv'
	driver_browser_init();
		
	get_page_links('6')
	
	time.sleep(10);
	#debug_test()	
	driver.quit()