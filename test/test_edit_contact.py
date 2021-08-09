# -*- coding: utf-8 -*-
import random
from model.contact import Contact


def test_edit_some_contact(app, db, check_ui):
    contact = Contact(first_name="first_name", middle_name="middle_name", last_name="last_name",
            nickname="nickname", title="title", company="company",
            address="address", home="home", mobile="mobile", work="work",
            fax="fax", email="email", email2="email2", email3="email3",
            homepage="homepage", address2="address2", phone2="phone2",
            notes="notes", bday="8", bmonth="March", byear="1990", aday="9", amonth="March",
            ayear="2090")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    contact_index = random.choice(old_contacts)
    index = old_contacts.index(contact_index)
    app.contact.edit_contact_by_id(contact, index)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == len(new_contacts)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

