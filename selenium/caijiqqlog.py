#coding:utf-8
from selenium import webdriver
import time,os,re,urllib,urllib2,hashlib

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

#driver.minimize_window() 
#driver=webdriver.Firefox()
def get_shuoshuo(qq,path):
    #testexist(path)
	try:
		#driver.set_page_load_timeout(10)
		#driver.get('https://user.qzone.qq.com/822989010/2')
		driver.get('file:///home/bcg/samba/test/selenium/qqdemo.html')
		time.sleep(1)
	except:
		print ("err")
		time.sleep(2)
		driver.quit()
		return
		
		
		
		
	#try:
		#driver.switch_to.frame("tblog")
		#time.sleep(10)
		#print "switchto frame ok"
		#print driver.page_source
		
	#except:
		#print driver.page_source+"err"
		#driver.quit()
	#else:
		#print "dddddddddddddddddddddddddddddddddddddd"
		#print driver.page_source+"else"
		#driver.switch_to.frame("tblog")
		#time.sleep(30)
		#print "switchto frame ok"
		#print( driver.find_element_by_id('page-container-blog').text)
		#driver.find_element_by_id('switcher_plogin').click()
		#driver.find_element_by_id('u').clear()
		#driver.find_element_by_id('u').send_keys('#####') 
		#driver.find_element_by_id('p').clear()
		#driver.find_element_by_id('p').send_keys('#####') 
		#driver.find_element_by_id('login_button').click()
		#driver.implicitly_wait(3)
		#	driver.quit()
		
		
	try:
		#print driver.page_source
		#Links = driver.find_element_by_xpath("//a[starts-with(@href,'http://user.qzone.qq.com/822989010/blog/')]")		
		#Links = driver.findElements(By.xpath("//a[starts-with(@href,'http://us')]"))
		for link in driver.find_elements_by_xpath("//a[starts-with(@href,'http://user.qzone.qq.com/822989010/blog/')]"):
			print (link.get_attribute('href'))
			#print (elem.get_attribute("title"))
				
		driver.quit()
	except:
		print ("find_element_by_xpath no find")
		driver.quit()
#    try:
#        driver.find_element_by_id('QM_OwnerInfo_Icon')
#    except:
#      
#        time.sleep(2)
#        driver.quit()
#    else:
#        driver.switch_to.frame('app_canvas_frame')
#    #    last_page=driver.find_element_by_css_selector('.mod_pagenav')
#    #    page_num=re.findall('\d+',last_page.text)[-1]
#        next_page='page'
#        page=1
#        try:
#            while next_page:
#                content = driver.find_elements_by_css_selector('.content')
#                stime = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
#                for con,sti in zip(content,stime):
#                    data = {
#                        'time':sti.text,
#                        'shuos':con.text
#                    }
#                    write_data(data['time'],data['shuos'],path)
#                next_page=driver.find_element_by_link_text(u'下一页')
#                page=page+1
#                print u'正在抓取第%d页面内容······'%page
#                next_page.click()
#
#                time.sleep(3)
#                driver.implicitly_wait(3)
#            driver.quit()
#        except:
#            print u'抓取到%d页面结束'%page
#            driver.quit()

#def  testexist(path):
#    if not os.path.exists(path):
#        w= xlwt.Workbook()
#        w.add_sheet('Sheet1')
#        w.save(path)
#    else:
#        os.remove(path)
#        w= xlwt.Workbook()
#        w.add_sheet('Sheet1')
#        w.save(path)
def write_data(data1,data2,path):
    f=xlrd.open_workbook(path)
    sheet=f.sheet_by_name('Sheet1')
    src=copy(f)
    row=sheet.nrows
    src.get_sheet(0).write(row,0,data1)
    src.get_sheet(0).write(row,1,data2)
    src.save(path)
def create_id():
    m = hashlib.md5(str(time.clock()).encode('utf-8'))
    return m.hexdigest()	
#通过url获取网页
def getHtml(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	req = urllib2.Request(url = url, headers = headers)
	content = urllib2.urlopen(req).read()
	return content
	
def get_log_context():
	try:
		driver.get('file:///home/bcg/samba/test/selenium/qqdemo_context.html')
		#print (driver.page_source)
		elem = driver.find_elements_by_id("blogDetailDiv")
		#print (elem)
		#print (elem.text)
		#print (elem.get_attribute('innerHTML'))
		#print (driver.find_elements_by_xpath("//div[@id='blogDetailDiv']").get_attribute('innerHTML'))
		
	except:
		print ("get_log_context err")
		time.sleep(2)
		driver.quit()
		return
	
			
	try:
		str_text = driver.page_source
		for link in driver.find_elements_by_xpath("//img[starts-with(@src,'http')]"):
			print ("loading...  "+link.get_attribute('src'))						
			cat_img = getHtml(link.get_attribute('src'))
			print ("down load ok")
			
			filename=create_id()+'.jpg'
			with open("pic/"+filename,'wb') as f:
				f.write(cat_img)
				print("save pic ok,"+filename)
	except:
		print ("loading pic err")
		driver.quit()
if __name__ == '__main__':
	# work_path=raw_input(u'请输入存储数据路径--excle表格类型')2571278041
	#work_path='E:\\0930\\WWWW.csv'
	#get_shuoshuo('######',work_path)#输入好友QQ号
	#get_log_context()
	cat_img = getHtml("http://a3.qpic.cn/psb?/V11BnhDf16EbKg/TREmi7HFovaVOHQumc77eh4mEyvUQNoPq0xGZr.Yjt8!/b/dK4AAAAAAAAA&ek=1&kp=1&pt=0&bo=aQGvAQAAAAAFF*I!&t=5&su=4202235713&tm=1513915200&sce=0-12-12&rf=2-9")
	

	filename=create_id()+'.jpg'
	with open("pic/"+filename,'wb') as f:
		f.write(cat_img)
	print("save pic ok,"+filename)