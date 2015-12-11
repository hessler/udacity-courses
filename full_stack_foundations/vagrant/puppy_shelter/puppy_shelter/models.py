"""
This module provides model classes for the Puppy Shelter project.
"""

#pylint: disable=relative-import,no-init,too-few-public-methods

import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base

class Shelter(Base):
    """A class to store information for a shelter."""

    __tablename__ = 'shelters'
    shelter_id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(80), nullable=False)
    zip_code = Column(String(10), nullable=False)
    website = Column(String(250), nullable=False)
    maximum_capacity = Column(Integer, nullable=False, default=25)
    current_occupancy = Column(Integer, nullable=False, default=0)

    @property
    def serialize(self):
        """Method to return serialized JSON object of class data."""

        return {
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'website': self.website,
            'maximum_capacity': str(self.maximum_capacity),
            'current_occupancy': str(self.current_occupancy)
        }

class Puppy(Base):
    """A class to store information for a puppy."""

    __tablename__ = 'puppies'
    puppy_id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    date_of_birth = Column(Date, nullable=False,
                           default=datetime.date.today()-datetime.timedelta(days=7))
    picture = Column(String(250), nullable=False,
                     default="http://pngimg.com/upload/small/dog_PNG2446.png")
    gender = Column(String(6), nullable=False)
    weight = Column(Integer, nullable=False)
    owner = Column(String(250), default='')
    shelter_id = Column(Integer, ForeignKey('shelters.shelter_id'))
    shelter = relationship(Shelter)

    @property
    def serialize(self):
        """Method to return serialized JSON object of class data."""

        return {
            'name': self.name,
            'date_of_birth': str(self.date_of_birth),
            'gender': self.gender,
            'weight': str(self.weight),
            'owner': self.owner,
            'shelter_id': str(self.shelter_id)
        }
