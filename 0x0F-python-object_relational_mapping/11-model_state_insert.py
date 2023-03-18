#!/usr/bin/python3
"""
Lists all state object from the database
using sqlalchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == "__main__":
    # creates an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # take the imported base class and create them in the database
    Base.metadata.create_all(engine)

    # create a session maker
    Session = sessionmaker(bind=engine)  # it returns a class

    # make an instance of the session class
    session = Session()

    # create an instance of the class
    data_in = State(name='Louisiana')

    # add to database
    session.add(data_in)

    # get data in order, but return the first
    data_out = session.query(State).filter(State.name == 'Louisiana')
    for x in data_out:
        print("{}".format(x.id))

    # commit to database
    session.commit()

    session.close()
