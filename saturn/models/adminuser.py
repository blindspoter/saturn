# -*- coding: utf-8 -*-

from datetime import datetime

from saturn.libs.db.store import db

from .consts import ADMINUSER_STATUS


class AdminUser(object):

    '''
    管理员账户
    '''

    def __init__(self, id, name, pwd, status, create_time):
        self.id = str(id)
        self.name = name
        self.pwd = pwd
        self.status = status
        self.create_time = create_time

    def __repr__(self):
        return '<AdminUser id=%s>' % self.id

    @classmethod
    def get(cls, id):
        r = db.execute('select id, name, password, status, create_time '
                       'from admin_user where id=%s', (id,))
        if r:
            return cls(*r[0])

    @classmethod
    def get_by_name(cls, name):
        r = db.execute('select id, name, password, status, create_time '
                       'from admin_user where name=%s', (name,))
        if r:
            return cls(*r[0])

    @classmethod
    def gets(cls, ids):
        return [cls.get(id) for id in ids]

    @classmethod
    def get_ids_by_status(cls, status):
        rs = db.execute('select id from admin_user where '
                        'status=%s order by create_time '
                        'desc', (status,))
        return [str(r[0]) for r in rs] if rs else []

    @classmethod
    def gets_by_status(cls, status):
        ids = cls.get_ids_by_status(status)
        return cls.gets(ids)

    @classmethod
    def add(cls, name, pwd):
        id = db.execute('insert into admin_user (name, password, status, create_time) '
                        'values (%s, %s, %s, %s)',
                        (name, pwd, ADMINUSER_STATUS.CREATED, datetime.now()))
        if id:
            db.commit()
            user = cls.get(id)
            return user

    def update(self, name):
        if self.name != name:
            db.execute('update admin_user set name=%s where id=%s',
                       (name, self.id))
            db.commit()
        return self.get(self.id)

    def delete(self):
        db.execute('delete from admin_user where id=%s', (self.id,))
        db.commit()
