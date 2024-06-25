#!/usr/bin/env python3

"""Create a SQLAlchemy model named User
for a database table named users
(by using the mapping declaration of SQLAlchemy).
"""
from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    """class User"""
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    hashed_password = Column(String(128))
