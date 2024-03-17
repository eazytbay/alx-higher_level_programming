#!/usr/bin/python3
'''
Script that prints the first State object from the database hbtn_0e_6_usa
'''

import sys
from model_state import Base, State
from sqlalchemy.orm import session
from sqlalchemy import create_engine


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, db_name))

    Base.metadata.create_all(engine)

    session = Session(engine)

    state = session.query(State).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
