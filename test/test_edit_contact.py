# -*- coding: utf-8 -*-
from model.contact import contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(contact(first_name="first", middle_name="middle", last_name="last", nickname="nick", title="title",
                            company="company", address="address", home="home", mobile="mobile", work="work", fax="fax",
                            email="email", email2="email2", email3="email3", homepage="homepage", address2="address2",
                            phone2="phone2", notes="notes", bday="9", bmonth="March", byear="1990", aday="9",
                            amonth="March", ayear="2090"))
    app.contact.edit_first_contact(contact(first_name="first_edit", middle_name="middle_edit", last_name="last_edit",
                                  nickname="nick_edit", title="title_edit", company="company_edit",
                                  address="address_edit", home="home_edit", mobile="mobile_edit", work="work_edit",
                                  fax="fax_edit", email="email_edit", email2="email2_edit", email3="email3_edit",
                                  homepage="homepage_edit", address2="address2_edit", phone2="phone2_edit",
                                  notes="notes_edit", bday="8", bmonth="May", byear="1989", aday="8", amonth="May",
                                  ayear="2089"))
