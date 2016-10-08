# -*- coding: utf-8 -*-

from tornado.web import RequestHandler


class Root(RequestHandler):
    def get(self):
        self.write("Hello!")


class Ping(RequestHandler):
    def get(self):
        self.write("Pong")
