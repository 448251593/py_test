#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.PhantomJS()
driver = webdriver.Firefox()    
driver.minimize_window();

driver.get("http://www.hao123.com")

#now_handle = driver.current_window_handle 
#print now_handle  

#driver.find_element_by_link_text(u"百　度").click()

driver.find_element_by_xpath("//input[starts-with(@class,'button button-hook')]").click()
time.sleep(5);

#driver.switch_to_window(driver.window_handles[0])
print('window0= '+driver.title);

driver.switch_to_window(driver.window_handles[1])
print('window1= '+driver.title);

#driver.find_element_by_id("kw").click();
#driver.find_element_by_id("kw").clear();
#driver.find_element_by_id("kw").send_keys("zxcvcc");
#driver.find_element_by_id("su").click();
#time.sleep(20);

#size = driver.find_element_by_name("wd").size
#print size

#news = driver.find_element_by_xpath("//div[@id='u1']/a[1]").text
#print news

#print driver.page_source
#href = driver.find_element_by_xpath("//div[@id='u1']/a[2]").get_attribute('href')
#name = driver.find_element_by_xpath("//div[@id='u1']/a[2]").get_attribute('name')
#print href,name
#
#
#location = driver.find_element_by_xpath("//div[@id='u1']/a[3]").location
#print location


#print driver.current_url

#print driver.title

#for link in driver.find_elements_by_xpath('//*[@href]'):
	#print (link.get_attribute('href'))
#result = location = driver.find_element_by_id("su").is_displayed()
#print result
driver.quit()