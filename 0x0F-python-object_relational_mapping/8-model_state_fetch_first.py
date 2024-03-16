#!/usr/bin/python3
'''
Script that prints the first State object from the database hbtn_0e_6_usa
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
    query = sess_obj.query(State).first()
    if query is None:
        print("Nothing")
    else:
        print(query.id, query.name, sep=": ")
