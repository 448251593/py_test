#coding:utf-8
from selenium import webdriver
import time,os,re,urllib,urllib2,hashlib,sys

#import xlrd,xlwt
#from xlutils.copy import copy
#使用selenium
#使用selenium的隐藏PhantimJS浏览器登陆账号后对内容获取
#注意frame与iframe的格式框切换
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
def get_shuoshuo(qq,path):
    #testexist(path)
	try:
		#driver.set_page_load_timeout(10)
		#https://user.qzone.qq.com/822989010/2
		driver.get('https://user.qzone.qq.com/822989010/2')
		#driver.get('file:///home/bcg/samba/test/selenium/qqdemo.html')
		time.sleep(1)
	except:
		print ("err")
		return
		
	try:
		driver.switch_to.frame(0)
		driver.find_element_by_link_text("4").click()
		time.sleep(4)
	except:
		print('page find err')
		return
		
	try:
		#print driver.page_source
		#Links = driver.find_element_by_xpath("//a[starts-with(@href,'http://user.qzone.qq.com/822989010/blog/')]")		
		#Links = driver.findElements(By.xpath("//a[starts-with(@href,'http://us')]"))
		Links = driver.find_elements_by_xpath("//a[starts-with(@href,'http://user.qzone.qq.com/822989010/blog/')]")
		for link in Links:
			print (link.get_attribute('href'))
			get_log_context('https://user.qzone.qq.com/822989010/blog/1488525155')
			#print (elem.get_attribute("title"))
				

	except:
		print ("find_element_by_xpath no find")


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
	
def get_log_context(url):
	print ('getting  ' + url)
	pathfile = create_path_base_url(url)
	if len(pathfile)==0:
		print("get path from url err")
		return
	pathfile = './'+pathfile	
	print('pathfile='+pathfile)
	os.system("mkdir -p "+pathfile)
	
	try:
		driver.get(url)
		#print (driver.page_source)		
		time.sleep(1)
		elem = driver.find_elements_by_id("tblog")
		print("find tblog")

	except:
		print ("get_log_context err")
		return

	#with open("page_source_1.txt",'wb') as f:
	#	f.write(driver.page_source)
	
	try:
		driver.switch_to.frame(0)
		print("switch tblog ok")
	except:
		print("switch_to.frame err")
		return

	with open("page_source_2.txt",'wb') as f:
		f.write(driver.page_source)
		
	try:
		#for link in driver.find_element_by_xpath("//img[starts-with(@data-src,'http')]"):
		#	print ("loading...  "+link.get_attribute('src'))						

		#s = re.findall(r'\btina','tian tinaaaa')
		div_str = driver.find_element_by_id('blogDetailDiv').get_attribute('innerHTML')
			
		str_txt=div_str
		urlarr = re.findall(r'data-src=".*?"',str_txt)
		for  elem in urlarr:			
			tmp_url = elem[len('data-src=')+1:len(elem)-1]
			file_path_url = get_file_and_save(tmp_url,pathfile)
			str_txt = str_txt.replace(tmp_url,file_path_url)
			print(tmp_url)
			print(file_path_url)
		print('find_element_by_id ok')	
		with open(pathfile+"/page_source.html",'wb') as f:
			f.write(str_txt)
		print(pathfile+"/page_source.html "+'save ok')
	except:
		print ("loading pic err")		
		return
	
	
	
def get_file_and_save(url, path):
	cat_img = getHtml(url)
	print ("down load ok")

	filename=path+"/"+create_id()+'.jpg'
	with open(filename,'wb') as f:
		f.write(cat_img)
		print("save pic ok,"+filename)	
	return filename
	
	

def create_path_base_url(url):
	strid = re.findall(r'/blog/[0-9]*',url)
	path = strid[0][1:len(strid[0])]
	return path
	
	
	
def debug_test():
	pathfile = create_path_base_url('https://user.qzone.qq.com/822989010/blog/1488525103')
	if len(pathfile)==0:
		print("get path from url err")
		return
	pathfile = './'+pathfile	
	print('pathfile='+pathfile)
	
	
	with open(pathfile+"/page_source_3.html",'r') as f:
		str_txt=f.read()
		urlarr = re.findall(r'data-src=".*?"',str_txt)
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
	get_shuoshuo('sdf','ddd')
	#get_log_context('https://user.qzone.qq.com/822989010/blog/1488525155')
	#debug_test()
	
	driver.quit()