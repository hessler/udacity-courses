"""
This module provides classes for the Restaurant project.
"""

#pylint: disable=relative-import,no-init,too-few-public-methods

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database_utils import BASE

class Restaurant(BASE):
    """A class to store restaurant information."""

    __tablename__ = 'restaurant'
    name = Column(String(80), nullable=False)
    restaurant_id = Column(Integer, primary_key=True)


class MenuItem(BASE):
    """A class to store information for a menu item."""

    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    menu_item_id = Column(Integer, primary_key=True)
    course = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    price = Column(String(8), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurant.restaurant_id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        """Method to return serialized JSON object of class data."""

        return {
            'name': self.name,
            'description': self.description,
            'menu_item_id': self.menu_item_id,
            'price': self.price,
            'course': self.course
        }
