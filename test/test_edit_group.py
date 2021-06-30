# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    # создаем группу с пустыми параметрами
    app.group.create(Group(name="", header="", footer=""))
    # редактируем параметры для группы
    app.group.edit_group(Group(name="name_edit", header="header_edit", footer="footer_edit"))
    app.session.logout()

