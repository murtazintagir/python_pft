import random
from fixture.orm import ORMFixture

def test_delete_contact_from_group(app, ORMFixture):
    ORMFixture.checker_that_we_have_groups_with_contacts(app)
    groups_with_contacts = ORMFixture.get_groups_with_contacts()
    group = random.choice(groups_with_contacts)
    contacts_in_group = ORMFixture.get_contacts_in_groups(group)
    contact = random.choice(contacts_in_group)
    app.contact.delete_contact_from_group(contact.id, group)
    new_contacts_with_groups = ORMFixture.get_contacts_in_groups(group)
    contacts_in_group.remove(contact)
    assert contacts_in_group == new_contacts_with_groups