import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from HtmlTestRunner import HTMLTestRunner
import time 


class bigsearch(unittest.TestCase):

    def setUp(self):
        self.googletest = webdriver.Chrome("C:/seleniumdriver/chromedriver.exe")
        self.googletest.set_page_load_timeout(15)
        self.googletest.get("https://www.google.com/")
        self.googletest.maximize_window()
        self.googletest.refresh()

    def test_1_searchcodingcenter(self):
        self.googletest.find_element("xpath", "//textarea[@id='APjFqb']").send_keys("best coding center in lagos")
        self.googletest.find_element("name", "q").send_keys(Keys.ENTER)

    def test_2_searchbestmusicstar(self):
        self.googletest.find_element("xpath", "//textarea[@id='APjFqb']").send_keys("the best hiphop artists in nigeria")
        self.googletest.find_element("name", "q").send_keys(Keys.ENTER)

    def test_3_searchrichestmen(self):
        self.googletest.find_element("name", "q").send_keys("richest men in africa")
        self.googletest.find_element("name", "q").send_keys(Keys.ENTER)

    def test_4_OS(self):
        self.googletest.find_element("name", "q").send_keys("What is the most efficient mobile operating system?")
        self.googletest.find_element("name", "q").send_keys(Keys.ENTER)

    def test_5_testingtools(self):
        self.googletest.find_element("name", "q").send_keys("testing framework")
        self.googletest.find_element("name", "q").send_keys(Keys.ENTER)

    def test_6_ASI(self):
        self.googletest.find_element("name", "q").send_keys("what is artificial super intelligence?")
        self.googletest.find_element("name", "q").send_keys(Keys.ENTER)

    def tearDown(self):
        time.sleep(5)
        print("Test Completed Successfully!")
        self.googletest.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(
        output="./report",report_name="Google Search Test",report_title="Total Google Tests"
        ))


        