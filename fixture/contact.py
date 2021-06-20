from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, Data):
        wd = self.app.wd
        self.open_page()
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
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Data.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Data.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Data.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Data.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Data.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Data.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Data.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Data.homepage)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Data.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Data.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Data.notes)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(Data.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(Data.bmonth)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Data.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(Data.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(Data.amonth)
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Data.ayear)
        # submit contact creation
        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # submit first contact
        wd.find_element_by_name("selected[]").click()
        # delete contact
        wd.find_element_by_name("delete").click()

    def open_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("add new").click()