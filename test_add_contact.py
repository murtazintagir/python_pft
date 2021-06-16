# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Data, Contact


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
        self.create_data_info(wd, Data(first_name="first", middle_name="middle", last_name="last", nickname="nick", title="title", company="company", address="address"))
        self.create_contact_info(wd, Contact(home="home", mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3", homepage="homepage", address2="address2", phone2="phone2", notes="notes"))
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def create_data_info(self, wd, Data):
        # fill address book
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Data.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Data.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Data.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Data.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Data.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Data.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Data.address)
        # submit group creation
        #wd.find_element_by_name("submit").click()

    def create_contact_info(self, wd, Contact):
        # fill address book
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contact.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contact.homepage)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contact.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contact.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Contact.notes)
        # submit contact creation
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
