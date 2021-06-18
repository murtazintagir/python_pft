# -*- coding: utf-8 -*-
import pytest
from contact import Data
from application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_address_book(app):
    app.login(username="admin", password="secret")
    app.create_data_info(Data(first_name="first", middle_name="middle", last_name="last", nickname="nick", title="title", company="company", address="address", home="home", mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3", homepage="homepage", address2="address2", phone2="phone2", notes="notes", bday="9", bmonth="March", byear="1990",aday="9", amonth="March", ayear="2090"))
    app.logout()

