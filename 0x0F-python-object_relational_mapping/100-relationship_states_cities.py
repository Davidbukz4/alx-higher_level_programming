#!/usr/bin/python3
"""
Lists all state object from the database
using sqlalchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # creates an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # take the imported base class and create them in the database
    Base.metadata.create_all(engine)

    # create a session maker
    Session = sessionmaker(bind=engine)  # it returns a clas

    # make an instance of the session class
    session = Session()

    created_state = State(name='California')
    created_city = City(name='San Francisco')
    created_state.cities.append(created_city)

    session.add(created_city)

    session.commit()

    session.close()
