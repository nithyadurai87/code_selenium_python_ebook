import unittest
from selenium import webdriver

class SearchTests (unittest.TestCase):
    def setUp(self):
	desired_caps = {}
	desired_caps['platform'] = 'WINDOWS'
	desired_caps['browserName'] = 'internet explorer'
	self.a = webdriver.Remote('http://192.168.1.5:4444/wd/hub',desired_caps)
	self.a.ignoreZoomSetting=True
        self.a.get("http://magento-demo.lexiconn.com/")
        self.a.maximize_window()
	

    def test_search(self):
	self.a.find_element_by_xpath("//input[@id='search']").send_keys("Bed & Bath")
	self.a.find_element_by_xpath("//input[@id='search']").submit()
	lis = self.a.find_elements_by_xpath("//h2[@class='product-name']/a")
	self.assertEqual(12, len(lis))

    def tearDown(self):
	self.a.close()

if __name__ == '__main__':
	unittest.main(verbosity=2)


