from sqlalchemy import create_engine, MetaData, Table, sql
from sqlalchemy.orm import sessionmaker
import settings
import schema


class Database(object):
    """Databse class for all relations and commands"""
    __engine = None
    __connect = None
    __session = None

    def __new__(self):
        """Singletone implementation for database"""
        if not hasattr(self, 'instance'):
            self.instance = super(Database, self).__new__(self)
        return self.instance

    def __init__(self):
        """Connecting to database"""
        self.__engine = create_engine(settings.db_engine)
        self.__connect = self.__engine.connect()
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    def install(self):
        """Installing tables on database

        Returns:
            True/False about tables creation status.
        """
        schema.Base.metadata.create_all(self.__engine)
        return True

    def insert(self, schema, data):
        """Insert method for adding new data in database.

        Args:
            schema: schema class.
            data: dictionary of data.
        Returns:
            Return True/False which related to status of insert action.
        """
        self.__session.add(schema(**data))
        self.__session.commit()
        return True

    def delete(self, schema, where):
        """Delete method for deleting data from database.

        Args:
            schema: schema class.
            where: dictionary of determind map for remove.
        Returns:
            Return True/False which related to status of delete action.
        """
        rows = self.__session.query(schema).filter_by(**where).first()
        self.__session.delete(rows)
        self.__session.commit()
        return True
