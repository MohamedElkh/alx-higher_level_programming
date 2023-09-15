#!/usr/bin/python3
"""
conatin the class of definition of city
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    the class that define each city
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
