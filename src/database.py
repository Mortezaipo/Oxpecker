import psycopg2 as pgsql
import psycopg2.extras as pgsql_extras


class Database(object):
    """Database library for connecting to PostgreSQL database"""

    _con = None
    _cur = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not self._con:
            self.connect()

    def connect(self):
        """Connecting to database"""
        try:
            self._con = pgsql.connect(database="oxpecker", user="morteza", password="136", host="localhost")
            self._cur = self._con.cursor(cursor_factory=pgsql_extras.DictCursor)
        except pgsql.DatabaseError as err:
            raise "Connection failed! Check connection settings. [%s]" % err

    def disconnect(self):
        """Closing database open connection"""
        if self._con:
            self._con.close()

    def fetch(self, query, fetch_one=False):
        """Fetch records on SQL query

        :param query: SQL command.
        :param fetch_one: fetching just 1 records.
        :return: records of result which fetched from database.
        """
        if not self._con:
            self.connect()
        print(query)
        try:
            self._cur.execute(query)
            if fetch_one:
                result = self._cur.fetchone()
            else:
                result = self._cur.fetchall()
            return result
        except pgsql.DatabaseError as err:
            raise Exception("Fetch all query failed! Check your SQL query. " + str(err))

    def delete(self, query):
        """Delete SQL execution.

        :param query: SQL command.
        :return: True/False about action result.
        """
        if not self._con:
            self.connect()

        try:
            self._cur.execute(query)
            self._con.commit()
        except pgsql.DatabaseError as err:
            raise Exception("Delete query failed! Check your SQL query. " + str(err))

    def insert(self, query):
        """Insert SQL execution.

        :param query: SQL command.
        :return: True/False about action result.
        """
        if not self._con:
            self.connect()

        try:
            self._cur.execute(query)
            self._con.commit()
        except pgsql.DatabaseError as err:
            raise Exception("Insert query failed! Check your SQL query. " + str(err))

    def update(self, query):
        """Update SQL execution.

        :param query: SQL command.
        :return: True/False about action result.
        """
        if not self._con:
            self.connect()

        try:
            self._cur.execute(query)
            self._con.commit()
        except pgsql.DatabaseError as err:
            raise Exception("Insert query failed! Check your SQL query. " + str(err))

    def execute(self, query):
        """Execute SQL query.

        :param query: SQL command.
        :return: True/False about action result.
        """
        if not self._con:
            self.connect()

        try:
            self._cur.execute(query)
            self._con.commit()
        except pgsql.DatabaseError as err:
            raise Exception("Execute query failed! Check your SQL query. " + str(err))