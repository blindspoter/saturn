# -*- coding: utf-8 -*-

from handlers.index import Root, Ping
from handlers.admin_user import AdminUserCreate, AdminUserDelete

# URL参数使用名字
# url_prefix
handlers = [
    (r"/", Root),
    (r"/ping", Ping),

    (r"/v1/admin/user/create", AdminUserCreate),
    (r"/v1/adminuser/(.*)/delete", AdminUserDelete)
]
