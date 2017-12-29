from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re    
def test_toutiao(self):
        driver = self.driver
        driver.get("https://mp.toutiao.com/profile_v2/home")
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div[2]/div/div").click()
        driver.find_element_by_id("title").click()
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"文章标题")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=4 | ]]
        driver.find_element_by_xpath("//body").click()
        # ERROR: Caught exception [unknown command [editContent]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath("//div[@id='edui51_body']/div").click()
        driver.find_element_by_xpath("//div[@id='rt_rt_1c2ea9aib1i01fl716fphbhng1']/label").click()
        driver.find_element_by_id("local-ok").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]").click()
        driver.find_element_by_id("title").click()
        driver.find_element_by_id("title").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=title | ]]
        driver.find_element_by_id("title").click()
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"文章标题文章标题")
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]").click()
        driver.find_element_by_xpath("//i[@type='add']").click()
        driver.find_element_by_xpath("//img[@alt='53e90001e9fe1c5ff2eb']").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("//div[@id='root']/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
