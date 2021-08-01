# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ":" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits
    return prefix + ":" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ":" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" \
           + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 10),
                    last_name=random_string("last_name", 10), nickname=random_string("nickname", 10),
                    title=random_string("title", 10), company=random_string("company", 10),
                    address=random_string("address", 10), home=random_phone("home", 10), mobile=random_phone("mobile", 10),
                    work=random_phone("work", 10), fax=random_phone("fax", 10), email=random_email("email", 5),
                    email2=random_email("email2", 5), email3=random_email("email3", 5), homepage=random_string("homepage", 10),
                    address2=random_string("address2", 10), phone2=random_phone("phone2", 10), notes=random_string("notes", 10),
                    bday="9", bmonth="March",  byear="1990", aday="9", amonth="March", ayear="2090")
            for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_address_book(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
