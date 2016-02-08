import tornado.web
from src import users

url = tornado.web.Application([
    (r"/users/", users.User),
    (r"/users/information/", users.UserInformation),
    (r"/users/authentication/", users.UserAuthentication),
])
