# -*- coding: utf-8 -*-


from tornado.web import HTTPError


class APIError(HTTPError):

    """
    status_code：http状态码
    errcode:    全局错误码
    errmsg：    错误信息

    """

    def __init__(self, msg='', status_code=400):
        super(APIError, self).__init__(status_code=400, log_message=msg)
        self.errcode = 40000
        self.errmsg = msg or '请求异常'
        self.status_code = status_code

    def __str__(self):
        return '{errcode: %s, errmsg: %s}' % (self.errcode, self.errmsg)

    __repr__ = __str__


class InvalidError(APIError):

    def __init__(self, msg='', status_code=401):
        super(InvalidError, self).__init__(msg, status_code)
        self.errcode = 40005
        self.errmsg = msg or 'Invalid field'
        self.status_code = status_code or 401


class NotFoundError(APIError):

    def __init__(self, msg='', status_code=404):
        super(NotFoundError, self).__init__(msg, status_code)
        self.errcode = 40001
        self.errmsg = msg or 'URI没有找到'
        self.status_code = status_code or 404


class ArgumentError(APIError):

    def __init__(self, msg='', status_code=400):
        super(ArgumentError, self).__init__(msg, status_code)
        self.errcode = 40002
        self.errmsg = msg or '参数错误'
        self.status_code = status_code


class TargetNotFoundError(APIError):

    def __init__(self, msg='', status_code=400):
        super(TargetNotFoundError, self).__init__(msg, status_code)
        self.errcode = 40003
        self.errmsg = msg or '目标没有找到'
        self.status_code = status_code


class NoPermissionError(APIError):

    def __init__(self, msg='', status_code=403):
        super(NoPermissionError, self).__init__(msg, status_code)
        self.errcode = 40004
        self.errmsg = msg or '需要权限'
        self.status_code = status_code


class CreatedError(APIError):

    def __init__(self, msg='', status_code=422):
        super(CreatedError, self).__init__(msg, status_code)
        self.errcode = 40011
        self.errmsg = msg or '创建失败'
        self.status_code = status_code


class UserStatusError(APIError):

    def __init__(self, msg='', status_code=400):
        super(UserStatusError, self).__init__(msg, status_code)
        self.errcode = 40030
        self.errmsg = msg or '用户状态异常'
        self.status_code = status_code
