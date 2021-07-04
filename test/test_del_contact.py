# -*- coding: utf-8 -*-
def test_delete_first_contact(app):
    app.contact.delete_first_contact()


#def test_delete_search_contact(app):
#    app.session.login(username="admin", password="secret")
#    app.contact.delete_search_contact()
#    app.session.logout()
