#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if os.getenv("HBTN_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, overlaps="place_amenities")
    else:
        amenity_ids = []

        @property
        def reviews(self):
            """Getter attribute.
            Returns the list of Review instances with place_id matching the
            current Place.id"""
            from models import storage

            my_reviews = []
            for review in storage.all(Review).values():
                if self.id == review.place_id:
                    my_reviews.append(review)
            return my_reviews

        @property
        def amenities(self):
            """Getter attribute.
            Returns the list of Amenity instances with amenity_id matching the
            current Amenity.id linked to the place"""
            from models import storage

            my_amenities = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    my_amenities.append(amenity)
            return my_amenities

        @amenities.setter
        def amenities(self, obj):
            """ Setter for amenity.ids """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
