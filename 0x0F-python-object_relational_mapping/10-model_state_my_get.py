#!/usr/bin/python3
"""
print the state object
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                         format(sys.argv[1], sys.argv[2], sys.argv[3]),
                         pool_pre_ping=True)

    Session = sessionmaker(bind=eng)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    print("Not found" if not state else  state.id)
