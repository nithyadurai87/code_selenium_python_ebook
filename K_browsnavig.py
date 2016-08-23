
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class compare (unittest.TestCase):
    def setUp(self):
        self.a = webdriver.Firefox()
        self.a.implicitly_wait(30)
        self.a.get("http://www.google.com")
        self.a.maximize_window()

    def test_browser_navigation(self):
	self.a.find_element_by_xpath("//input[@title='Search']").send_keys("selenium webdriver")
	self.a.find_element_by_xpath("//input[@title='Search']").submit()
	self.a.find_element_by_link_text("Selenium WebDriver").click()

	self.a.back()
        self.a.implicitly_wait(60)
	self.a.forward()
        self.a.implicitly_wait(60)
	self.a.refresh()
        self.a.implicitly_wait(60)
	
    def tearDown(self):
    	self.a.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
