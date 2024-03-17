#!/usr/bin/python3
'''
Script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
'''

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(mysql_username, mysql_password, db_name))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

