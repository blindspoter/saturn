# -*- coding: utf-8 -*-

import requests

from .framework import BaseTestCase

USERNAME = 'apitestuser'
PASSWORD = '123456'


class AdminUserTest(BaseTestCase):
    def test_adminuser_create(self):
        url = self.api_prefix + '/adminuser/create'
        params = {'username': USERNAME, 'password': PASSWORD}

        response = requests.post(url, params=params)
        assert response.status_code == 200

    def test_adminuser_delete(self):
        url = self.api_prefix + '/adminuser/{name}/delete'.format(name=USERNAME)
        response = requests.delete(url)
        assert response.status_code == 200
