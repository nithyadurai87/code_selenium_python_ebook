
import unittest
from selenium import webdriver
from time import gmtime,strftime

class Login (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = webdriver.Firefox()
        cls.a.implicitly_wait(30)
        cls.a.get("http://magento-demo.lexiconn.com/")
        cls.a.maximize_window()

    def test_register(self):
        self.a.find_element_by_link_text("ACCOUNT").click()
        self.a.find_element_by_link_text("Log In").click()

	x = self.a.find_element_by_link_text("CREATE AN ACCOUNT")
	self.assertTrue(x.is_displayed() and x.is_enabled())
	x.click()
	self.assertEquals("Create New Customer Account",self.a.title)

	fn = self.a.find_element_by_id("firstname")
	ln = self.a.find_element_by_id("lastname")
	ea = self.a.find_element_by_id("email_address")
	pa = self.a.find_element_by_id("password")
	co = self.a.find_element_by_id("confirmation")
	su = self.a.find_element_by_id("is_subscribed")
	re = self.a.find_element_by_xpath("//button[@title='Register']")

	self.assertEqual("255", fn.get_attribute("maxlength"))
	self.assertEqual("255", ln.get_attribute("maxlength"))
	self.assertTrue(fn.is_enabled() and ln.is_enabled() and ea.is_enabled() and pa.is_enabled() and
	co.is_enabled() and su.is_enabled() and re.is_enabled())
	self.assertFalse(su.is_selected())

	laname = "user_" + strftime("%Y%m%d%H%M%S", gmtime()) 
	fn.send_keys("Test")
	ln.send_keys(laname)
	su.click()
	ea.send_keys(laname + "@example.com")
	pa.send_keys("tester")
	co.send_keys("tester")
	re.click()

	self.assertEqual("Hello, Test " + laname + "!",self.a.find_element_by_css_selector("p.hello >strong").text)
	self.a.find_element_by_link_text("ACCOUNT").click()
	self.assertTrue(self.a.find_element_by_link_text("Log Out").is_displayed())
	
    @classmethod
    def tearDownClass(cls):
    	cls.a.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
