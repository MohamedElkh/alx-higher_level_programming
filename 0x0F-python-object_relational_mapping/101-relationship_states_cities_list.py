#!/usr/bin/python3
"""
lists all state objects city
"""
import sys
from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                         sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

    Session = sessionmaker(bind=eng)
    see = Session()

    for st in see.query(State).order_by(State.id):
        print("{}: {}".format(st.id, st.name))
        for city in st.cities:
            print("   {}: {}".format(city.id, city.name))
