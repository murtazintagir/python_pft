# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_address_book(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def test_add_address_book(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_address_book_page(wd)
        self.create_address_book(wd, Contact(first_name="first", middle_name="middle", last_name="last", nickname="nick"))
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def create_address_book(self, wd, Contact):
        # fill address book
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_address_book_page(self, wd):
        # open group page
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
