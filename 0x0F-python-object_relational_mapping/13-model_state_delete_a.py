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
                                   argv[3]))

    Base.metadata.create_all(engine)
    # Initial configuration arguments
    Session = sessionmaker(bind=engine)
    # This session is bound to provided engine
    session = Session()
    a = '%a%'
    tb = session.query(State).filter_by(State.name.like(a))
    for state in tb:
        session.delete(state)
    session.commit()
    session.close()
