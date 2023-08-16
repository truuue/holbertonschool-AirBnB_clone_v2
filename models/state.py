#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    """ db ==>  means let's go for SQLAlchemy logic"""
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE', '') != 'db':
        @property
        def cities(self):
            """Returns the list of City instances with state_id matching the current State.id"""
            from models import storage
            from models.city import City

            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
