from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("Users\seleniumdriver/chromedriver.exe")
# driver = webdriver("./selenium/chromedriver")

driver.set_page_load_timeout(15)

driver.get("http://www.google.com")

driver.maximize_window()
driver.refresh()

time.sleep(3)

driver.find_element("name", "q").send_keys("python selenium")
driver.find_element("name", "q").send_keys(Keys.ENTER)

# driver.find_element_by_name("btnK").click()

time.sleep(3)

driver.quit()


