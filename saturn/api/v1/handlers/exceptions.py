# -*- coding: utf-8 -*-


class APIException(Exception):

    def __init__(self, error, msg='', http_code=400):
        self.code = 1000
        self.errmsg = msg or '请求异常'
        self.http_code = http_code

    def __str__(self):
        return '{}[code:{}; errmsg:{};]'.format(
            self.__class__.__name__, self.code, self.errmsg)


class InvalidError(APIException):

    def __init__(self, msg='', http_code=401):
        self.code = 998
        self.errmsg = msg or 'Invalid field'
        self.http_code = http_code or 401


class NotFoundError(APIException):

    def __init__(self, msg='', http_code=404):
        self.code = 1001
        self.errmsg = msg or 'URI没有找到'
        self.http_code = http_code or 404


class ArgumentError(APIException):

    def __init__(self, msg='', http_code=400):
        self.code = 1002
        self.errmsg = msg or '参数错误'
        self.http_code = http_code


class TargetNotFoundError(APIException):

    def __init__(self, msg='', http_code=400):
        self.code = 1003
        self.errmsg = msg or '目标没有找到'
        self.http_code = http_code


class NoPermissionError(APIException):

    def __init__(self, msg='', http_code=403):
        self.code = 1004
        self.errmsg = msg or '需要权限'
        self.http_code = http_code


class CreatedError(APIException):

    def __init__(self, msg='', http_code=422):
        self.code = 1011
        self.errmsg = msg or '创建失败'
        self.http_code = http_code


class UserStatusError(APIException):

    def __init__(self, msg='', http_code=400):
        self.code = 1030
        self.errmsg = msg or '用户状态异常'
        self.http_code = http_code
