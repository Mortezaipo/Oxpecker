from sqlalchemy import create_engine, MetaData, Table, sql
import settings
#import schema

class Database(object):
    __engine = None
    __connect = None

    def __init__(self):
        self.__engine = create_engine(settings.db_engine)
        self.__connect = self.__engine.connect()


    ####TEST
    def test(self):
        meta = MetaData(self.__engine)
        users = Table('users', meta, autoload=True)

        s = sql.select([users])
        r = self.__connect.execute(s)

        print r.fetchall()
