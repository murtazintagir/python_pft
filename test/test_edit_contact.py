# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app, db, check_ui):
    contact = Contact(first_name="first_edit", middle_name="middle_edit", last_name="last_edit",
                      nickname="nick_edit", title="title_edit", company="company_edit",
                      address="address_edit", home="home_edit", mobile="mobile_edit", work="work_edit",
                      fax="fax_edit", email="email_edit", email2="email2_edit", email3="email3_edit",
                      homepage="homepage_edit", address2="address2_edit", phone2="phone2_edit",
                      notes="notes_edit", bday="8", bmonth="May", byear="1989", aday="8", amonth="May",
                      ayear="2089")
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.edit_contact_by_id(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

