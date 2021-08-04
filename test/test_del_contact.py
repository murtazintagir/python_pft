# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    contact = Contact(first_name="first", middle_name="middle", last_name="last", nickname="nick",
                                   title="title", company="company", address="address", home="home", mobile="mobile",
                                   work="work", fax="fax", email="email", email2="email2", email3="email3",
                                   homepage="homepage", address2="address2", phone2="phone2", notes="notes", bday="9",
                                   bmonth="March", byear="1990", aday="9", amonth="March", ayear="2090")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    index = random.choice(old_contacts)
    app.contact.delete_contact_by_id(index.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(index)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)
