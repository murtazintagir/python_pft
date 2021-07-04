# -*- coding: utf-8 -*-
from model.contact import contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(contact(first_name="first_edit", middle_name="middle_edit", last_name="last_edit",
                                  nickname="nick_edit", title="title_edit", company="company_edit",
                                  address="address_edit", home="home_edit", mobile="mobile_edit", work="work_edit",
                                  fax="fax_edit", email="email_edit", email2="email2_edit", email3="email3_edit",
                                  homepage="homepage_edit", address2="address2_edit", phone2="phone2_edit",
                                  notes="notes_edit", bday="8", bmonth="May", byear="1989", aday="8", amonth="May",
                                  ayear="2089"))
