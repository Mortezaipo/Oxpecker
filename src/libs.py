from src.database import Database
import re
from hashlib import md5


class Libs:

    def __init__(self):
        self.db = Database()

    @staticmethod
    def authentication(username, password):
        """Sign up action.

        :param username: username of registered user.
        :type username: str
        :param password: password of registered user.
        :type password: str
        :return: True/False which means authenticate action is success of failure.
        :rtype: bool
        """
        db = Database()
        sql = "SELECT * FROM users where username='{}' and password='{}'"
        sql = sql.format(username, md5(password.encode('utf-8')).hexdigest())
        row = db.fetch(sql, True)
        if row:
            return row
        else:
            return False

    @staticmethod
    def get_users_list():
        """Fetch list of all users from database

        :return: list of users
        :rtype: list
        """
        db = Database()
        sql = "SELECT * FROM users"
        rows = db.fetch(sql)
        return list(rows)

    @staticmethod
    def check_user_existence(info):
        """Check user existence in database.

        :param info: a list which contain username and email.
        :type info: list
        :return: Boolean list which show username exists or not and email exists or not.
        :rtype: list
        """
        db = Database()
        result = list()
        for data in info:
            if '@' in data:
                sql = "SELECT id FROM users WHERE email='{}'".format(data)
            else:
                sql = "SELECT id FROM users WHERE username='{}'".format(data)
            row = db.fetch(sql, True)
            if row:
                result.append(True)
            else:
                result.append(False)
        return result

    @staticmethod
    def check_data(data, mode='username'):
        """Check user data.

        :param data: data which you wish to check it.
        :type data: str
        :param mode: type of checking (username or email)
        :type mode: str
        :return: True/False which show your data is matched with your mode or not.
        :rtype: bool
        """
        if data.find(' ') is not -1:
            return False
        data = data.lower()
        if mode is 'username':
            pattern = re.compile('[a-z\0-9_]+')
        elif mode is 'email':
            pattern = re.compile('[a-z\0-9_-]+@[a-z0-9\._-]+\.[a-z]{2,}')
        if pattern.match(data):
            return True
        return False

    @staticmethod
    def create_user(username, password, email):
        """Create user account.

        :param username: username of desired user which need to register.
        :param password: password of desired user which need to register.
        :param email: email of desired user which need to register.
        :return: True/False which shows registration is success or failure.
        :rtype: str
        """
        check = Libs.check_user_existence((username, email))
        if (check[0] | check[1]) is True:
            return 'exist_err'
        if not Libs.check_data(username) or not Libs.check_data(email):
            return 'data_err'

        db = Database()
        sql = "INSERT INTO users (username, is_active, is_lock, email, password) VALUES ('{}', true, false, '{}', '{}')"
        sql = sql.format(username, email, md5(password.encode('utf-8')).hexdigest())
        action = db.insert(sql)
        if action:
            return 'register_suc'
        else:
            return 'register_err'
