from sqlalchemy import create_engine, select, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine('sqlite:///users.db', echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

Base.metadata.create_all(engine)

