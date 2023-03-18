#!/usr/bin/python3
"""
City model
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """ Class to run in ORM """
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
