# -*- coding: utf-8 -*-

from tornado.options import define

define('debug', default=False, help='enable debug mode')
define('port', default=5000, help='run on this port', type=int)
