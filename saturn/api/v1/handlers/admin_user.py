# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
from saturn.models.adminuser import AdminUser

from.exceptions import ArgumentError, CreatedError


class AdminUserCreate(RequestHandler):

    # /v1/admin/user/create

    def post(self):
        args = self.request.arguments
        name = args.get("username")
        pwd = args.get("password")
        if not name or not pwd:
            raise ArgumentError

        user = AdminUser.add(name, pwd)
        if not user:
            raise CreatedError

        result = {"message": "creating admin user successful!"}
        self.finish(result)


class AdminUserDelete(RequestHandler):

    # /v1/admin/user/(.*)/delete

    def delete(self, username):
        if not username:
            raise ArgumentError

        user = AdminUser.get_by_name(username)
        if user:
            user.delete()

        result = {"message": "delete admin user successful!"}
        self.finish(result)
