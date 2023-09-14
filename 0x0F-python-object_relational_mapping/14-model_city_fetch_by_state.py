#!/usr/bin/python3
"""
prints all cities objects from database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                        format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

    Session = sessionmaker(bind=eng)
    see = Session()

    scity = see.query(State, City).filter(State.id == City.state_id).all()

    for state, city in scity:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
