"""
This module provides database setup and configuration.
"""

import datetime

from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm.query import Query
from sqlalchemy.exc import OperationalError

from utilities.db.sql_alchemy_helpers import get_or_create

#-----------------------------------------------------------------------
# Must be at start of file
#-----------------------------------------------------------------------
# Create instance of declarative base. Lets sqlalchemy know that python
# classes are special sqlalchemy classes that correspond to tables in DB.
BASE = declarative_base()


# Other Global Variables
DB_URL = 'sqlite:///puppy_shelter/puppies.db'
ENGINE = None
DB_SESSION = None
SESSION = None


class Shelter(BASE):
    """A class to store information for a shelter"""

    __tablename__ = 'shelters'
    shelter_id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(80), nullable=False)
    zip_code = Column(String(10), nullable=False)
    website = Column(String(250), nullable=False)
    maximum_capacity = Column(Integer, nullable=False, default=100)
    current_occupancy = Column(Integer, nullable=False, default=0)

    def __init__(self, **kwargs):
        """
        Initializes Shelter with supplied argument values.

        Args:
            **kwargs: Keyword args for class attributes.
        """
        # Required attributes (via nullable=False values above)
        self.name = kwargs.get('name') or ''
        self.address = kwargs.get('address') or ''
        self.city = kwargs.get('city') or ''
        self.state = kwargs.get('state') or ''
        self.zip_code = kwargs.get('zip_code') or ''
        self.website = kwargs.get('website') or ''
        self.maximum_capacity = kwargs.get('maximum_capacity') or ''
        self.current_occupancy = kwargs.get('current_occupancy') or ''

    def get_info(self):
        """A simple method to print shelter information."""
        return "Shelter:\n - {}\n - {}\n - {}\n - {}\n - {}\n - {}\n - {}"\
            "\n - {}".format(
            self.name, self.address, self.city,
            self.state, self.zip_code, self.website,
            self.maximum_capacity, self.current_occupancy
        )

class Puppy(BASE):
    """A class to store information for a puppy."""

    __tablename__ = 'puppies'
    puppy_id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    picture = Column(String(250), nullable=False)
    gender = Column(String(6), nullable=False)
    weight = Column(Integer, nullable=False)
    shelter_id = Column(Integer, ForeignKey('shelters.shelter_id'))
    shelter = relationship(Shelter)

    def __init__(self, **kwargs):
        """
        Initializes Puppy with supplied argument values.

        Args:
            **kwargs: Keyword args for class attributes.
        """
        # Required attributes (via nullable=False values above)
        self.name = kwargs.get('name') or ''
        self.date_of_birth = kwargs.get('date_of_birth') or \
            datetime.date(2015, 1, 1)
        self.picture = kwargs.get('picture') or ''
        self.gender = kwargs.get('gender') or ''
        self.weight = kwargs.get('weight') or 0
        self.shelter = kwargs.get('shelter') or None

    def get_info(self):
        """A simple method to print puppy information."""
        return "{} ({}) - {}, {}, {}".format(
            self.name, str(self.date_of_birth),
            self.gender, "{} lbs".format(self.weight), self.shelter.name
        )


def establish_session(auto_create_data=True):
    """Function to establish DB session and kick off data creation."""

    global SESSION, ENGINE, DB_SESSION
    if not SESSION:
        try:
            ENGINE = create_engine(DB_URL)
            BASE.metadata.create_all(ENGINE)
        except OperationalError:
            ENGINE = create_engine('sqlite:///puppies.db')
            BASE.metadata.create_all(ENGINE)
        BASE.metadata.bind = ENGINE

        # Setup session
        DB_SESSION = sessionmaker(bind=ENGINE)
        SESSION = DB_SESSION()
        if auto_create_data:
            create_data(False)


def create_data(check_session=True):
    """Function to create and set up DB and populate with data."""

    if check_session:
        establish_session()

    # Query for shelter items. If none exist, create via prefab data.
    all_shelters = SESSION.query(Shelter).first()
    all_puppies = SESSION.query(Puppy).first()
    if not all_shelters or not all_puppies:
        from prefab_puppy_data import create_all_the_things
        create_all_the_things(SESSION)


def fetch_all_puppies_alphabetical():
    """
    Function to query all of the puppies and print them in
    alphabetical order by name.
    """

    establish_session()
    all_puppies = SESSION.query(Puppy).order_by(Puppy.name).all()

    print "\nPuppies (Alphabetical):"
    print "-----------------------"
    for puppy in all_puppies:
        print " - {}".format(puppy.get_info())

    print " "


def fetch_puppies_age():
    """
    Function to query all of the puppies and retrieve any six months old
    or younger, ordered by the youngest first.
    """

    establish_session()
    today = datetime.date.today()
    six_months_ago = datetime.date(today.year, today.month, today.day)

    if today.month - 6 <= 0:
        six_months_ago = datetime.date(
            today.year - 1, today.month + 6, today.day
        )
    else:
        six_months_ago = datetime.date(
            today.year, today.month - 6, today.day
        )

    all_puppies = SESSION.query(Puppy)\
        .filter(Puppy.date_of_birth >= six_months_ago)\
        .order_by(Puppy.date_of_birth.desc())\
        .all()

    print "\nPuppies (Six Months and Younger, Ordered by Youngest First):"
    print "------------------------------------------------------------"
    for puppy in all_puppies:
        age = today - puppy.date_of_birth
        print " - {}: {} days old (D.O.B. {})".format(
            puppy.name, age.days, puppy.date_of_birth.strftime("%m-%d-%Y")
        )

    print " "


def fetch_puppies_weight():
    """
    Function to query all of the puppies ordered by ascending weight.
    """

    establish_session()

    all_puppies = SESSION.query(Puppy).order_by(Puppy.weight).all()

    print "\nPuppies (Ordered by Ascending Weight):"
    print "--------------------------------------"
    for puppy in all_puppies:
        print " - {}: {} lbs".format(
            puppy.name, puppy.weight
        )

    print " "


def fetch_puppies_by_shelter():
    """
    Function to query all of the puppies and group them by the shelter
    in which they are staying.
    """

    establish_session()

    all_shelters_list = SESSION.query(Shelter).all()
    all_puppies = SESSION.query(Puppy).order_by(Puppy.shelter_id).all()
    all_shelters = {}
    for shelter in all_shelters_list:
        all_shelters[shelter.shelter_id] = shelter

    print "\nPuppies (Ordered by Shelter):"
    print "-----------------------------"
    for puppy in all_puppies:
        print " - {}: {}".format(
            puppy.name, all_shelters[puppy.shelter_id].name
        )

    print " "



# Run function to create data
if __name__ == '__main__':
    establish_session()
