#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    datab_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(datab_engine)

    Session = sessionmaker(bind=datab_engine)
    session = Session()

    fr_State = State(name='California')
    fr_City = City(name='San Francisco')
    fr_State.cities.append(fr_City)

    session.add(fr_State)
    session.add(fr_City)
    session.commit()
