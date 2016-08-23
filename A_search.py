from selenium import webdriver

a = webdriver.Firefox()
a.get("http://magento-demo.lexiconn.com/")
a.maximize_window()

a.find_element_by_xpath("//input[@id='search']").send_keys("Bed & Bath")
a.find_element_by_xpath("//button[@title='Search']").click()

lis = a.find_elements_by_xpath("//h2[@class='product-name'] / a ")

print str(len(lis)) + " products found"

for i in lis:
	print i.text

a.quit()






