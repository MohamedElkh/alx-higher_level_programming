#!/usr/bin/python3
"""
lists all the state objects from database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    see = Session()

    states = see.query(State).order_by(State.id).all()

    for st in states:
        print("{}: {}".format(st.id, st.name))
