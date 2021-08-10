from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders
import random


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        last_name = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
            return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))


    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), last_name=contact.last_name, first_name=contact.first_name)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_groups_with_contacts(self):
        groups_with_contacts = []
        group_id = self.db.select("group_id FROM address_in_groups")
        for i in group_id:
            groups_with_contacts.append(Group(id=str(i)))
        return groups_with_contacts

    def checker_that_we_have_groups_with_contacts(self, app):
        if len(self.get_groups_with_contacts()) == 0:
            old_contacts = self.get_contact_list()
            old_groups = self.get_group_list()
            app.contact.checker_that_old_contacts_not_zero(old_contacts)
            app.group.checker_that_old_groups_not_zero(old_groups)
            old_contactsNEW = self.get_contact_list()
            old_groupsNEW = self.get_group_list()
            available_groups = app.group.get_available_groups(old_groupsNEW, old_contactsNEW, self)
            group = random.choice(available_groups)
            contacts_not_in_group = self.get_contacts_not_in_group(group)
            contact = random.choice(contacts_not_in_group)
            app.contact.add_contact_to_group(contact.id, group)
