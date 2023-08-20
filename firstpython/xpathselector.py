from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#from selenium.webdriver.chrome.service import Service
#service = Service("C:/seleniumdriver/chromedriver.exe")
#driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome("C:/seleniumdriver/chromedriver.exe")
# driver = webdriver("./selenium/chromedriver")

driver.set_page_load_timeout(15)

driver.get("http://www.google.com")

driver.maximize_window()
driver.refresh()

time.sleep(3)

driver.find_element("xpath", "//textarea[@id='APjFqb']").send_keys("javascript")
driver.find_element("xpath", "//textarea[@id='APjFqb']").send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()