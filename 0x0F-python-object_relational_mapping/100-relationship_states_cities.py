#!/usr/bin/python3
"""
create the state california with san fransisco
"""
import sys
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                         sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    see = Session()

    c_st = State(name='California')
    c_cty = City(name='San Francisco')
    c_st.cities.append(c_cty)
    see.add(c_st)

    see.commit()
    see.close()
