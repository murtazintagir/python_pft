# -*- coding: utf-8 -*-
import random
from model.group import Group



def test_edit_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = random.choice(old_groups)
    group = Group(name="name_edit")
    app.group.edit_group_by_id(group, index.id)
    new_groups = db.get_group_list()
    old_groups.append(group)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
