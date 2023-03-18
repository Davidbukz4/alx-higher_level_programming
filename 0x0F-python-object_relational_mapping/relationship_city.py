#!/usr/bin/python3
"""
City class
"""
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_state import Base, State


class City(Base):
    """
    class to run in the ORM
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
