#!/usr/bin/python3
"""
lists all cities objects from database
"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                         format(sys.argv[1], sys.argv[2], sys.argv[3]),
                         pool_pre_ping=True)

    Session = sessionmaker(bind=eng)
    see = Session()

    for city in see.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))
