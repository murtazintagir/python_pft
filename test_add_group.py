# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_new_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    
    def test_add_new_group(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("adfgh")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("adfgh")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("adfgh")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("Logout").click()
    

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
