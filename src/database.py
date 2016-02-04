from sqlalchemy import create_engine, MetaData, Table, sql
from sqlalchemy.orm import sessionmaker
from src import settings


class Database(object):
    """Database class for all relations and commands"""
    _engine = None
    _connect = None
    _session = None

    def __new__(self):
        """Singletone implementation for database"""
        if not hasattr(self, 'instance'):
            self.instance = super(Database, self).__new__(self)
        return self.instance

    def __init__(self):
        """Connecting to database"""
        self._engine = create_engine(settings.db_engine)
        self._connect = self._engine.connect()
        session = sessionmaker(bind=self._engine)
        self._session = session()

    @property
    def session(self):
        return self._session