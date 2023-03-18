#!/usr/bin/python3
"""
Lists all state object from the database
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == '__main__':
    # create an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # take the imported base class and create them in the database
    Base.metadata.create_all(engine)

    # create a session maker
    Session = sessionmaker(bind=engine)  # it returns a class

    # make an instance of the Session class
    session = Session()

    # get data in order, returns the first record
    data = session.query(State).order_by(State.id).first()
    if not(output):
        print('Nothing')
    else:
        print('{}: {}'.format(data.id, data.name))

    # close the session
    seesion.close()
