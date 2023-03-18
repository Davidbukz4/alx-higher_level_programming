#!/usr/bin/python3
"""
State model
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# base class to inherit from
Base = declarative_base()  # it returns a class


class State(Base):
    """ Class to run in ORM """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
