class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        # open group page
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

    def filling_field(self, group):
        wd = self.app.wd
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
        wd = self.app.wd
        self.open_group_page()
        # submit first group
        wd.find_element_by_name("selected[]").click()
        # delete group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        # submit first group
        wd.find_element_by_name("selected[]").click()
        # edit group
        wd.find_element_by_name("edit").click()
        self.filling_field(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element_by_link_text("group page").click()
