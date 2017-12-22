import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
class PythonOrgSearch(unittest.TestCase):
 
    def setUp(self):
		elf.driver = webdriver.PhantomJS()
 	#self.driver = webdriver.Firefox()
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
	#element = driver.find_element_by_id("page-container-blog")
	#print(element.text)

	print("-----------------------------------------")
	#print(driver.page_source)
	element = driver.find_element_by_id("su")
	element.submit()
	time.sleep(20)
	#print(driver.page_source)
        #self.assertIn("Python", driver.title)
        #elem = driver.find_element_by_name("q")
       # elem.send_keys("pycon")
       # elem.send_keys(Keys.RETURN)
       # assert "No results found." not in driver.page_source
 
    def tearDown(self):
        self.driver.close()
 
if __name__ == "__main__":
    unittest.main()
