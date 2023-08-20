from selenium import webdriver
import time
from selenium import webdriver

#####FOR SELENIUM WITH VERSION 4.0.0 
from selenium.webdriver.chrome.service import Service
service = Service("C:/seleniumdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

#####FOR SELENIUM WITH VERSION LOWER THAN 4.0.0, you dont need to pass in a service object
driver = webdriver.Chrome("C:/Seleniumdrivers/chromedriver.exe")
# driver = webdriver("./selenium/chromedriver")

driver.set_page_load_timeout(15)

driver.get("http://www.anchorsoftacademy.com")

driver.refresh()
driver.maximize_window()

driver.find_element("xpath", "//ul[@class='navbar-nav ml-auto']//a[@class='nav-link'][normalize-space()='All Courses']").click()

time.sleep(10)

driver.close()