#!/usr/bin/python3
"""This module defines a class to manage DBStorage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor method for the DBStorage class"""
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """Returns a dictionary of all objects in
        the given class or in all classes"""
        if cls is not None:
            query = self.__session.query(cls).all()
        else:
            query = []
            classes = [State, City, User, Place, Review, Amenity]
            for Cls in classes:
                query.extend(self.__session.query(Cls).all())

        objects_dict = {}
        for obj in query:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objects_dict[key] = obj

        return objects_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session f not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload all data from the database and create a new session"""
        from sqlalchemy.ext.declarative import declarative_base

        Base = declarative_base()
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Close the session"""
        self.__session.remove()
