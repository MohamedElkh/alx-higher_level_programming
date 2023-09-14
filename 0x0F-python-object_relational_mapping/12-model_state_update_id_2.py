#!/usr/bin/python3
"""
do the change the name of state object from database
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

    update = session.query(State).filter(State.id == 2).first()

    if update:
        update.name = 'New Mexico'
        session.commit()
