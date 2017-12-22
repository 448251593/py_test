from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.PhantomJS()
driver = webdriver.Firefox()    
driver.get("https://www.baidu.com/")

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

for link in driver.find_elements_by_xpath('//*[@href]'):
	print (link.get_attribute('href'))
#result = location = driver.find_element_by_id("su").is_displayed()
#print result
driver.quit()