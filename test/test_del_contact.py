# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="first", middle_name="middle", last_name="last", nickname="nick",
                                   title="title", company="company", address="address", home="home", mobile="mobile",
                                   work="work", fax="fax", email="email", email2="email2", email3="email3",
                                   homepage="homepage", address2="address2", phone2="phone2", notes="notes", bday="9",
                                   bmonth="March", byear="1990", aday="9", amonth="March", ayear="2090"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
