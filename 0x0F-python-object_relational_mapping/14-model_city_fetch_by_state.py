#!/usr/bin/python3
"""
Lists all state object from the database
using sqlalchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City

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
    data_out = session.query(State.name, City.id, City.name)\
                      .join(City, State.id == City.state_id).order_by(City.id)
    for x in data_out:
        print('{}: ({}) {}'.format(x[0], x[1], x[2]))

    session.close()
