
import unittest
from selenium import webdriver
from time import gmtime,strftime

class Login (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = webdriver.Firefox()
        cls.a.implicitly_wait(30)
        cls.a.get("http://demo.magentocommerce.com/")
        cls.a.maximize_window()

    def test_register(self):
        self.a.find_element_by_link_text("ACCOUNT").click()
        self.a.find_element_by_link_text("Log In").click()

	x = self.a.find_element_by_link_text("CREATE AN ACCOUNT")
	self.assertTrue(x.is_displayed() and x.is_enabled())
	x.click()
	self.assertIsNot("Create New Custmer Account",self.a.title,['Hai'])

	su = self.a.find_element_by_id("is_subscribed")
	
	self.assertFalse(su.is_selected())

    @classmethod
    def tearDownClass(cls):
    	cls.a.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
