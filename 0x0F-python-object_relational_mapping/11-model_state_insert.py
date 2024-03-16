#!/usr/bin/python3
'''
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    datab_engine = create_engine(URL.create(**url_parameters))
    Base.metadata.create_all(datab_engine)
    Session = sessionmaker(bind=datab_engine)
    obj_sess = Session()
    mt = State(name='Louisiana')
    obj_sess.add(mt)
    obj_sess.commit()
    x = obj_sess.query(State).filter(State.name == "Louisiana")
    for item in x:
        print(item.id)
