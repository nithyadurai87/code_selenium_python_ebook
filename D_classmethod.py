
import unittest
from selenium import webdriver

class SearchTests (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = webdriver.Firefox()
        cls.a.get("http://magento-demo.lexiconn.com/")
        cls.a.maximize_window()

    def test_search_product1(self):
        self.a.find_element_by_xpath("//input[@id='search']").send_keys("Bed & Bath")
        self.a.find_element_by_xpath("//input[@id='search']").submit()
        lis = self.a.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(12, len(lis))

    def test_search_product2(self):
        self.a.find_element_by_xpath("//input[@id='search']").clear()
        self.a.find_element_by_xpath("//input[@id='search']").send_keys("Bags & Luggage")
        self.a.find_element_by_xpath("//input[@id='search']").submit()
        lis = self.a.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(12, len(lis))
    @classmethod

    def tearDownClass(cls):
    	cls.a.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
