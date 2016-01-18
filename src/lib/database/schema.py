from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


user_game_relation = Table('users_games', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('game_id', Integer, ForeignKey('games.id')),
)


# User table
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = Column(String(32), unique=True)
    join_date = Column(DateTime, default=func.now())
    is_active = Column(Boolean, default=True)
    is_lock = Column(Boolean, default=False)
    last_login_date = Column(DateTime, default=None, nullable=True)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, nullable=True)
    games_basket = relationship("Game", secondary=user_game_relation)


# Licenses table
class License(Base):
    __tablename__ = "licenses"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    body = Column(String)
    is_commercial = Column(Boolean)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, nullable=True)
    license = relationship("Game")


# Game table
class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    author_name = Column(String(30))
    author_email = Column(String(45))
    author_website = Column(String(50), nullable=True)
    price = Column(Integer, default=0)
    license = Column(Integer, ForeignKey('licenses.id'))
