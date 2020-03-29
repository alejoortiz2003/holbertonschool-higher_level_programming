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
    table_state = session.query(State.name.like("%a%")).order_by(State.id)
    for state in table_state:
        print("{}: {}".format(table_state.id, table_state.name))
    session.close()
