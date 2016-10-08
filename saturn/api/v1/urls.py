# -*- coding: utf-8 -*-

from handlers.index import Root, Ping
from handlers.adminuser import AdminUserCreate, AdminUserDelete

handlers = [
    (r"/", Root),
    (r"/ping", Ping),
    (r"/api/v1/adminuser/create", AdminUserCreate),
    (r"/api/v1/adminuser/(.*)/delete", AdminUserDelete)
]
