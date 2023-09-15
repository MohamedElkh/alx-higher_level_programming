#!/usr/bin/python3
"""
state conatins class and base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
    class with id and name attr of each state
    """
    __tablename_ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="states", cascade="all, delete")
