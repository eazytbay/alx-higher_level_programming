#!/usr/bin/python3
"""This is a python file that contains the definition of the class
of a City and an instance Base = declarative_base()"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """A City class with name, id and state id"""

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    id_of_state = Column(Integer, ForeignKey('states.id'), nullable=False)
