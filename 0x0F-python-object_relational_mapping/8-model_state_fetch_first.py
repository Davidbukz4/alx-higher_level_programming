#!/usr/bin/python3
"""
Lists all state object from the database
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

    # get data in order, but return the first
    data = session.query(State).order_by(State.id).first()
    if not (data):
        print("Nothing")
    else:
        print("{}: {}".format(data.id, data.name))
    session.close()
