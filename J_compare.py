
import unittest
from selenium import webdriver

class compare (unittest.TestCase):
    def setUp(self):
        self.a = webdriver.Firefox()
        self.a.implicitly_wait(30)
        self.a.get("http://magento-demo.lexiconn.com/")
        self.a.maximize_window()

    def test_compare_products(self):

	self.a.find_element_by_xpath("//input[@id='search']").send_keys("phones")
	self.a.find_element_by_xpath("//button[@title='Search']").click()
	self.a.find_element_by_link_text("Add to Compare").click()
	self.a.find_element_by_xpath("//input[@id='search']").clear()
	self.a.find_element_by_xpath("//input[@id='search']").send_keys("Bed & Bath")
	self.a.find_element_by_xpath("//button[@title='Search']").click()
	self.a.find_element_by_link_text("Add to Compare").click()
	self.a.find_element_by_link_text("Clear All").click()
	i = self.a.switch_to_alert()
	self.assertEqual("Are you sure you would like to remove all products from your comparison?", i.text)
	i.accept()

    def tearDown(self):
    	self.a.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
