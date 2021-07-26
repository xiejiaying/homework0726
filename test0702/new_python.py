from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http//www.baidu.com")
driver.implicitly_wait(100)
print("xinzeng")