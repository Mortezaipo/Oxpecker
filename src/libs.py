from src.database import Database


class Libs:

    def __init__(self):
        self.db = Database()

    @staticmethod
    def authentication(username, password):
        db = Database()
        sql = "SELECT * FROM users where username='{}' and password='{}'".format(username, password)
        row = db.fetch(sql, True)
        if row:
            return True
        else:
            return False
