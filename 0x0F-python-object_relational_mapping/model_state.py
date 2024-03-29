#!/usr/bin/python3
"""
contain state class abd base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

data = MetaData()
Base = declarative_base(metadata=data)


class State(Base):
    """
    this class with id and name attr of each state
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
