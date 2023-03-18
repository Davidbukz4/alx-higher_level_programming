#!/usr/bin/python3
"""
State model
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship

meta_data = MetaData()
# base class to inherit from
Base = declarative_base(metadat=meta_data)  # it returns a class


class State(Base):
    """ Class to run in ORM """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
