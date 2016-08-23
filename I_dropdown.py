
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class dropdown (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = webdriver.Firefox()
        cls.a.implicitly_wait(30)
        cls.a.get("http://magento-demo.lexiconn.com/")
        cls.a.maximize_window()

    def test_language_options(self):
       	x = ["ENGLISH", "FRENCH", "GERMAN"]
	y = []
	d = Select(self.a.find_element_by_id("select-language"))
	self.assertEqual(3, len(d.options))
	for i in d.options:
	    y.append(i.text)
	self.assertListEqual(x, y)
	self.assertEqual("ENGLISH", d.first_selected_option.text)
	d.select_by_visible_text("German")
	self.assertTrue("store=german" in self.a.current_url)
	d = Select(self.a.find_element_by_id("select-language"))
	d.select_by_index(0)
	
    @classmethod
    def tearDownClass(cls):
    	cls.a.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
