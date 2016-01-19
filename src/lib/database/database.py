from sqlalchemy import create_engine, MetaData, Table, sql
from sqlalchemy.orm import sessionmaker
import settings
import schema


class Database(object):
    __engine = None
    __connect = None

    def __init__(self):
        self.__engine = create_engine(settings.db_engine)
        self.__connect = self.__engine.connect()
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    def install(self):
        schema.Base.metadata.create_all(self.__engine)

    def destroy(self):
        pass

    def clean(self):
        pass

    def insert(self, data):
        self.__session.add(schema.License(**data))
        self.__session.commit()

    def delete(self, data):
        record = self.__session.query(schema.License).filter_by(id=data).first()
        self.__session.delete(record)
        self.__session.commit()

    def udate(self, **data):
        pass

    def select_all(self, table):
        records = self.__session.query(table).all()
        return records

    def select(self):
        pass

    # TEST
    def test(self):
        meta = MetaData(self.__engine)
        users = Table('users', meta, autoload=True)

        s = sql.select([users])
        r = self.__connect.execute(s)

        print r.fetchall()
