# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class requests(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_requests(self):
        success = True
        wd = self.wd
        wd.get("https://dev-etp.roseltorg.ru/authentication/login")
        wd.find_element_by_id("login").click()
        wd.find_element_by_id("login").send_keys("monakova")
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").send_keys("1234567")
        wd.find_element_by_id("ext-gen67").click()
        wd.find_element_by_id("ext-gen590").click()
        wd.find_element_by_link_text("0334100000717000079").click()
        wd.find_element_by_link_text("0321300077117000018").click()
        wd.find_element_by_xpath("//div[@id='ext-gen112']/div[3]/table/tbody/tr/td[5]/div/a").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
