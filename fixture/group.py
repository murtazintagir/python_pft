from model.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        # open group page
        if not (self.groups_page_opened()):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        self.filling_field(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def filling_field(self, group):
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        # submit first group
        self.select_group_by_index(index)
        # delete group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        # submit first group
        self.select_group_by_id(id)
        # delete group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def edit_first_group(self):
        self.select_group_by_index(0)

    def edit_group(self, group, index):
        wd = self.app.wd
        self.open_group_page()
        # submit first group
        self.select_group_by_index(index)
        # edit group
        wd.find_element_by_name("edit").click()
        self.filling_field(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def edit_group_by_id(self, group, id):
        wd = self.app.wd
        self.open_group_page()
        # submit first group
        self.select_group_by_id(id)
        # edit group
        wd.find_element_by_name("edit").click()
        self.filling_field(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groups page
        if not (self.groups_page_opened()):
            wd.find_element_by_link_text("group page").click()

    def groups_page_opened(self):
        wd = self.app.wd
        return wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cashe = None

    def get_group_list(self):
        if self.group_cashe is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cashe = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cashe.append(Group(name=text, id=id))
        return list(self.group_cashe)

    def get_available_groups(self, old_groups, old_contacts, db):
        available_groups = []
        for i in old_groups:
            number_of_contacts_in_group = len(db.get_contacts_in_group(i))
            if number_of_contacts_in_group != len(old_contacts):
                available_groups.append(i)
        if len(available_groups) == 0:
            self.create(Group(name="name", header="header", footer="footer"))
            available_groups = db.get_group_list()
        return available_groups

    def checker_that_old_groups_not_zero(self, old_groups):
        if len(old_groups) == 0:
            self.create(Group(name="name", header="header", footer="footer"))
