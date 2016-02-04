#!/usr/bin/env python

from src import routes
import tornado.ioloop

if __name__ == "__main__":
    application = routes.url
    application.listen(9000)
    tornado.ioloop.IOLoop.current().start()