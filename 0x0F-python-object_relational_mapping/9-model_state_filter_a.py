#!/usr/bin/python3
"""
Script that list all stage from database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    # Initial configuration arguments
    Session = sessionmaker(bind=engine)
    # This session is bound to provided engine
    session = Session()
    tb = session.query(State).filter(State.name.like("%a%")).order_by(State.id)
    for state in tb:
        print("{}: {}".format(state.id, state.name))
    session.close()
