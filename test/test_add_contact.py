# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_address_book(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="first", middle_name="middle", last_name="last", nickname="nick", title="title",
                            company="company", address="address", home="home", mobile="mobile", work="work", fax="fax",
                            email="email", email2="email2", email3="email3", homepage="homepage", address2="address2",
                            phone2="phone2", notes="notes", bday="9", bmonth="March", byear="1990", aday="9",
                            amonth="March", ayear="2090")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
