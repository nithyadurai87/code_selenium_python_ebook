from selenium import webdriver 

a = webdriver.Firefox() 
a.get("https://valaipathivu.wordpress.com/wp-admin") 
a.maximize_window() 

a.find_element_by_xpath("//input[@id='user_login']").send_keys("valaipathivu") 
a.find_element_by_xpath("//input[@id='user_pass']").send_keys("Kadavuchol") 
a.find_element_by_xpath("//input[@id='wp-submit']").click() 

print "Login is successful" 

a.find_element_by_link_text("Posts").click() 
a.find_element_by_link_text("Add New").click() 
a.find_element_by_xpath("//input[@id='title']").send_keys("Tamil Kavithaikal") 
a.find_element_by_xpath("//input[@id='publish']").click() 

print "New post is Published" 

