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

    def initial_schema(self, name, data):
        """Find schema, initalize and then return its class.

        Args:
            name: schema name.
            data: dictionary of data.
        Returns:
            Return schema class.
        """
        if name == 'License':
            return schema.License(**data)
        elif name == 'User':
            return schema.User(**data)
        elif name == 'Game':
            return schema.Game(**data)

    def insert(self, schema_name, data):
        """Insert method for adding new data in database.

        Args:
            schema_name: name of schema.
            data: dictionary of data.
        Returns:
            Return True/False which related to status of insert action.
        """
        self.__session.add(self.initial_schema(schema_name, data))
        self.__session.commit()
        return True
