
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod

class HomePageTest (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = webdriver.Firefox()
        cls.a.get("http://magento-demo.lexiconn.com/")
        cls.a.maximize_window()

    def test_searchbox(self):
        self.assertTrue (self.is_element_present (By.ID,"search"))
        self.assertTrue (self.a.find_element_by_id("search").is_enabled())
	x = self.a.find_element_by_id("search").get_attribute("maxlength")
	self.assertEqual("128",x)

    def test_languagebox(self):
        self.assertTrue (self.is_element_present (By.ID,"select-language"))

    def test_addcart(self):
	self.a.find_element_by_css_selector("div.header-minicart span.icon").click()
	x = "You have no items in your shopping cart."
	y = self.a.find_element_by_css_selector("p.empty").text
	self.assertEqual(x,y)
	self.a.find_element_by_css_selector("div.minicart-wrapper a.close").click()

    def test_account(self):
	x = self.a.find_element_by_link_text("ACCOUNT")
	y = self.a.find_elements_by_partial_link_text("ACCOUNT")
	self.assertTrue(x.is_displayed())
	self.assertEqual(2,len(y))

    def test_imgs(self):
	x = self.a.find_element_by_class_name("promos")
	y = x.find_elements_by_tag_name("img")
	self.assertEqual(3,len(y))

	z = self.a.find_element_by_xpath("//img[@alt='Shop Private Sales - Members Only']")
	self.assertTrue(z.is_displayed())
	z.click()
	self.assertEqual("VIP",self.a.title)

    @classmethod
    def tearDownClass(cls):
    	cls.a.quit()

    def is_element_present(self, how, what):
        try: self.a.find_element(by=how, value=what)
	except NoSuchElementException, e: return False
	return True

if __name__ == '__main__':
    unittest.main(verbosity=2)




