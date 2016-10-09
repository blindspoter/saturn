# -*- coding: utf-8 -*-

import os
import sys

from envcfg.json.saturn import HTTPS_SERVER
from unittest import TestCase


TEST_DIR = os.path.dirname(os.path.realpath(__file__))
APP_DIR = os.path.dirname(TEST_DIR)

sys.path.insert(0, APP_DIR + '/stubs')
sys.path.insert(0, TEST_DIR + '/stubs')

reload(sys)
sys.setdefaultencoding('utf8')


class BaseTestCase(TestCase):
    http_server = HTTPS_SERVER
    api_prefix = '{server}/v1'.format(server=http_server)

    def setUp(self):
        pass

    def tearDown(self):
        pass
