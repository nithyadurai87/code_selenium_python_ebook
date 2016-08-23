
import csv, unittest
from selenium import webdriver
from ddt import ddt, data, unpack

def get_data(f_name):
    data=[]
    cont = csv.reader(open(f_name, "rb"))
    next(cont, None)
    for i in cont:
        data.append(i)
    return data

@ddt
class search (unittest.TestCase):
    def setUp(self):
        self.a = webdriver.Firefox()
        self.a.implicitly_wait(30)
        self.a.get("http://magento-demo.lexiconn.com/")
        self.a.maximize_window()
    @data (*get_data("testdata.csv"))
    @unpack
    def test_search(self,i,j):
        self.a.find_element_by_xpath("//input[@id='search']").send_keys(i)
        self.a.find_element_by_xpath("//input[@id='search']").submit()
        lis1 = self.a.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(int(j), len(lis1))
       
    def tearDown(self):
    	self.a.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
