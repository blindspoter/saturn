# -*- coding: utf-8 -*-

err_ok = (1000, 'err_ok')
err_invalid_name = (1001, 'err_invalid_name')


class BaseError(Exception):

    """
    The base exception of Error
    """

    def __init__(self, error):
        self.errno = error[0]
        self.errmsg = error[1]

    def __str__(self):
        return 'BaseError[errno:%s; errmsg:%s;]' % (self.errno, self.errmsg)


class ClusterCreateError(BaseError):
    def __str__(self):
        return 'ClusterCreateError[errno:%s errmsg:%s]' % (self.errno, self.errmsg)


class ValidationError(Exception):

    """
    The base exception of validation
    """


class PasswordValidationError(ValidationError):

    def __unicode__(self):
        return u'密码输入有误'


class MismatchedError(PasswordValidationError):

    def __unicode__(self):
        return u'两次密码输入不一致，请重新输入'
