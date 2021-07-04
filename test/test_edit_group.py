# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    # создаем группу с пустыми параметрами
    app.group.create(Group(name="", header="", footer=""))
    # редактируем параметры для группы
    app.group.edit_group(Group(name="name_edit"))

