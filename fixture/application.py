from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)

    def logout(self):
            wd = self.wd
            # logout
            wd.find_element_by_link_text("Logout").click()

    def create_group(self, group):
            wd = self.wd
            self.open_group_page()
            # init group creation
            wd.find_element_by_name("new").click()
            # fill group firm
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
            # submit group creation
            wd.find_element_by_name("submit").click()
            self.return_to_groups_page()

    def open_group_page(self):
            wd = self.wd
            # open group page
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
            wd = self.wd
            # return to groups page
            wd.find_element_by_link_text("group page").click()

    def login(self, username, password):
            wd = self.wd
            self.open_home_page()
            # login
            wd.find_element_by_name("user").clear()
            wd.find_element_by_name("user").send_keys(username)
            wd.find_element_by_name("pass").clear()
            wd.find_element_by_name("pass").send_keys(password)
            wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_data_info(self, Data):
        wd = self.wd
        self.open_address_book_page()
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

    def open_address_book_page(self):
        wd = self.wd
        # open group page
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
            wd = self.wd
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

    def destroy(self):
            self.wd.quit()