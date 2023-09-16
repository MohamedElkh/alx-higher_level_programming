#!/usr/bin/python3
"""
contain state class abd base
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

data = MetaData()
Base = declarative_base(metadata=data)


class State(Base):
    """
    this class with id and name attr of each state
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='save-update, merge,
                          all, delete')
