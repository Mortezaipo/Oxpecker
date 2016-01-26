import tornado.web
import users

url = tornado.web.Application([
    (r"^users/", user),
])
