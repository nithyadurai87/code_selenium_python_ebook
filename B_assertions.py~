import unittest
from selenium import webdriver

class SearchTests (unittest.TestCase):
    def setUp(self):
        self.a = webdriver.Firefox()
        self.a.get("http://magento-demo.lexiconn.com/")
        self.a.maximize_window()

    def test_search(self):
		self.a.find_element_by_xpath("//input[@id='search']").send_keys("Bed & Bath")
		self.a.find_element_by_xpath("//input[@id='search']").submit()
		lis = self.a.find_elements_by_xpath("//h2[@class='product-name']/a")
		self.assertEqual(15, len(lis))

    def tearDown(self):
		self.a.close()

if __name__ == '__main__':
	unittest.main(verbosity=2)


