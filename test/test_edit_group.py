# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    # редактируем параметры для группы
    app.group.edit_group(Group(name="name_edit"))

