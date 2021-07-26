from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(100)
driver.get("http://www.baidu.com")
driver.implicitly_wait(100)
print("xinzengggg")