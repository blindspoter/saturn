# -*- coding: utf-8 -*-

import json
import requests

from .framework import BaseTestCase

USERNAME = 'apitestuser'
PASSWORD = '123456'


class AdminUserTest(BaseTestCase):
    def test_admin_user_create(self):
        url = self.api_prefix + '/admin/user/create'
        data = {'username': USERNAME, 'password': PASSWORD}

        response = requests.post(url, data=json.dumps(data))
        assert response.status_code == 200

    def test_admin_user_delete(self):
        url = self.api_prefix + '/admin/user/{name}/delete'.format(name=USERNAME)
        response = requests.delete(url)
        assert response.status_code == 200
