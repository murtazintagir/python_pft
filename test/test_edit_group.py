# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group_index = random.choice(old_groups)
    index = old_groups.index(group_index)
    group = Group(name="name_edit")
    app.group.edit_group_by_id(group, index)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    # assert old_groups == new_groups
