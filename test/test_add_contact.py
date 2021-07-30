# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_address_book(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Tagir", middle_name="", last_name="Murtazin", nickname="Malder", title="title",
                      company="GA", address="SPb", home="89203051998", mobile="89821243284", work="89062706917",
                      fax="fax", email="tr.murtazin@yandex.ru", email2="tr.murtazin@mail.ru",
                      email3="tr.murtazin19902gmail.com", homepage="homepage", address2="address2", phone2="phone2",
                      notes="notes", bday="9", bmonth="March", byear="1990", aday="9", amonth="March", ayear="2090")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
