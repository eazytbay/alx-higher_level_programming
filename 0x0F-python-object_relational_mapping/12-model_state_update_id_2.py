#!/usr/bin/python3
'''
This script changes the name of a State object
from the database hbtn_0e_6_usa at id == 2
'''

from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine, insert
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    url_parameters = {'drivername': 'mysql+mysqldb',
                  'username': argv[1],
                  'password': argv[2],
                  'host': 'localhost',
                  'port': 3306,
                  'database': argv[3]}
    datab_engine = create_engine(URL.create(**url_parameters), echo=True)
    Base.metadata.create_all(datab_engine)
    Session = sessionmaker(bind=datab_engine)
    obj_sess = Session()
    x = obj_sess.query(State).filter(State.id == 2)\
                .update({'name': "New Mexico"})
    obj_sess.commit()
