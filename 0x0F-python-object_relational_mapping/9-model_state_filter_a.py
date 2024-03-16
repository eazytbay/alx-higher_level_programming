#!/usr/bin/python3
'''
Script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
'''

from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    url_parameters = {'drivername': 'mysql+mysqldb',
                  'username': argv[1],
                  'password': argv[2],
                  'host': 'localhost',
                  'port': 3306,
                  'database': argv[3]}
    datab_engine = create_engine(URL.create(**url_parameters))
    Base.metadata.create_all(datab_engine)
    Session = sessionmaker(bind=datab_engine)
    obj_sess = Session()
    query = obj_sess.query(State).filter(State.name.like('%a%'))
    for row in query:
        print(row.id, row.name, sep=": ")
