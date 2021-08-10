import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_in_group(app, db):
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    app.contact.checker_that_old_contacts_not_zero(old_contacts)
    app.group.checker_that_old_groups_not_zero(old_groups)
    available_groups = app.group.get_available_groups(old_groups, old_contacts, db)
    group = random.choice(available_groups)
    contacts_not_in_group = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts_not_in_group)
    app.contact.add_contact_to_group(contact.id, group)
    new_contacts_not_in_group = db.get_contacts_not_in_group(group)
    contacts_not_in_group.remove(contact)
    assert contacts_not_in_group == new_contacts_not_in_group