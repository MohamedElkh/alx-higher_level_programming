#!/usr/bin/python3
"""
create the state california with san fransisco
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                         sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    see = Session()

    newS = State(name='California')
    newC = City(name='San Francisco')

    newS.cities.append(newC)

    see.add(newS)
    see.add(newC)
    see.commit()
    see.close()
