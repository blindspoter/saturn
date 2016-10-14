#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import Application
from tornado.options import options
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

from saturn.api.v1 import urls


def create_app():
    settings = dict(
        debug=options.debug,
    )
    return Application(urls.handlers, **settings)


def main():
    options.parse_command_line()
    app = create_app()
    server = HTTPServer(app)
    server.listen(options.port)
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
