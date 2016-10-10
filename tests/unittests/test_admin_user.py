# -*- coding: utf-8 -*-

from saturn.models.admin_user import AdminUser
from saturn.models.consts import ADMINUSER_STATUS

from .framework import BaseTestCase

NAME = "testuser"
PWD = "testtest"

NEW_NAME = "updatetestuser"


class AdminUserTest(BaseTestCase):
    def test_admin_user_add(self):
        user = AdminUser.add(NAME, PWD)
        assert user
        assert user.name == NAME
        assert user.pwd == PWD

        users = AdminUser.gets_by_status(ADMINUSER_STATUS.CREATED)
        assert users
        assert users[0].status == ADMINUSER_STATUS.CREATED

        user.delete()
        u = AdminUser.get(user.id)
        assert not u

    def test_admin_user_update(self):
        user = AdminUser.add(NAME, PWD)
        assert user
        new_user = user.update(NEW_NAME)
        assert new_user
        assert new_user.name == NEW_NAME
        new_user.delete()
        u = AdminUser.get(new_user.id)
        assert not u
