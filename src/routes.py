import tornado.web
from src import users

url = tornado.web.Application([
    (r"/users/", users.UserInformation),
    (r"/users/authentication/", users.UserAuthentication),
])
