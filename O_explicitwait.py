
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest

class kanchipuram (unittest.TestCase):
    def setUp(self):
        self.a = webdriver.Firefox()
        self.a.get("http://magento-demo.lexiconn.com/")
        self.a.maximize_window()

    def test_account_link(self):
	WebDriverWait(self.a, 10).until(lambda s: s.find_element_by_id("select-language").get_attribute("length") == "3")
	b = WebDriverWait(self.a, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ACCOUNT")))
	b.click()
	
    def tearDown(self):
    	self.a.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
