# -*- coding: utf-8 -*-


class Colors(object):

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @classmethod
    def run(cls, text, key='run'):
        print '[' + cls.OKBLUE + key + cls.ENDC + ']\t' + text

    @classmethod
    def success(cls, text):
        print '[' + cls.OKGREEN + 'ok' + cls.ENDC + ']\t' + text

    @classmethod
    def warn(cls, text):
        print '[' + cls.WARNING + 'warn' + cls.ENDC + ']\t' + text

    @classmethod
    def fail(cls, text):
        print '[' + cls.FAIL + 'fail' + cls.ENDC + ']\t' + text


bcolors = Colors
