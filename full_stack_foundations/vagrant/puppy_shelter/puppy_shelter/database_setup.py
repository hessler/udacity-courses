"""
This module provides pre-fab data for puppy and shelter items
that can be added to the database for testing.
"""

#pylint: disable=global-statement,unused-variable

import datetime
import random
from random import randint

from puppy_shelter.models import Shelter, Puppy
from puppy_shelter.database import get_or_create

MALE_NAMES = [
    "Bailey", "Max", "Charlie", "Buddy", "Rocky", "Jake",
    "Jack", "Toby", "Cody", "Buster", "Duke", "Cooper",
    "Riley", "Harley", "Bear", "Tucker", "Murphy", "Lucky",
    "Oliver", "Sam", "Oscar", "Teddy", "Winston", "Sammy",
    "Rusty", "Shadow", "Gizmo", "Bentley", "Zeus", "Jackson",
    "Baxter", "Bandit", "Gus", "Samson", "Milo", "Rudy",
    "Louie", "Hunter", "Casey", "Rocco", "Sparky", "Joey",
    "Bruno", "Beau", "Dakota", "Maximus", "Romeo", "Boomer",
    "Luke", "Henry"
]

FEMALE_NAMES = [
    'Bella', 'Lucy', 'Molly', 'Daisy', 'Maggie', 'Sophie',
    'Sadie', 'Chloe', 'Bailey', 'Lola', 'Zoe', 'Abby',
    'Ginger', 'Roxy', 'Gracie', 'Coco', 'Sasha', 'Lily',
    'Angel', 'Princess', 'Emma', 'Annie', 'Rosie', 'Ruby',
    'Lady', 'Missy', 'Lilly', 'Mia', 'Katie', 'Zoey',
    'Madison', 'Stella', 'Penny', 'Belle', 'Casey',
    'Samantha', 'Holly', 'Lexi', 'Lulu', 'Brandy',
    'Jasmine', 'Shelby', 'Sandy', 'Roxie', 'Pepper',
    'Heidi', 'Luna', 'Dixie', 'Honey', 'Dakota'
]

PUPPY_IMAGES = [
    "http://pngimg.com/upload/small/dog_PNG2446.png",
    "http://pngimg.com/upload/small/dog_PNG2444.png",
    "http://pngimg.com/upload/small/dog_PNG2416.png",
    "http://pngimg.com/upload/small/dog_PNG2413.png",
    "http://pngimg.com/upload/small/dog_PNG2414.png",
    "http://pngimg.com/upload/small/dog_png2403.png",
    "http://pngimg.com/upload/small/dog_png2399.png"
]


def create_random_age():
    """Function to create and return random Date for birthday."""
    today = datetime.date.today()
    days_old = randint(0, 540)
    birthday = today - datetime.timedelta(days=days_old)
    return birthday

def create_random_weight():
    """Function to create and return random weight b/w 1-40."""
    return randint(1, 40)

def get_available_shelters(session):
    """
    Function to query and return a list of shelters with available
    space for a new puppy.
    """
    shelters = session.query(Shelter)\
        .filter(Shelter.current_occupancy < Shelter.maximum_capacity).all()
    return shelters



def populate_database(session):
    """Function to create Shelter and Puppy objects."""

    print "Populating database with Shelters and Puppies..."

    # Create shelters.
    shelter_1 = get_or_create(session, Shelter,
                              name="Oakland Animal Services",
                              address="1101 29th Ave",
                              city="Oakland",
                              state="California",
                              zip_code="94601",
                              website="http://oaklandanimalservices.org")

    shelter_2 = get_or_create(session, Shelter,
                              name="San Francisco SPCA Mission "\
                              "Adoption Center",
                              address="250 Florida St",
                              city="San Francisco",
                              state="California",
                              zip_code="94103",
                              website="http://sfspca.org")

    shelter_3 = get_or_create(session, Shelter,
                              name="Wonder Dog Rescue",
                              address="2926 16th Street",
                              city="San Francisco",
                              state="California",
                              zip_code="94103",
                              website="http://wonderdogrescue.org")

    shelter_4 = get_or_create(session, Shelter,
                              name="Humane Society of Alameda",
                              address="PO Box 1571",
                              city="Alameda",
                              state="California",
                              zip_code="94501",
                              website="http://hsalameda.org")

    shelter_5 = get_or_create(session, Shelter,
                              name="Palo Alto Humane Society",
                              address="1149 Chestnut St.",
                              city="Menlo Park",
                              state="California",
                              zip_code="94025",
                              website="http://paloaltohumane.org")

    # Create male and female puppies. For each, assign one of the
    # available shelters that has capacity for more puppies.
    for i, rand_name in enumerate(MALE_NAMES):
        shelters = get_available_shelters(session)
        rand_shelter_id = randint(0, len(shelters) - 1)
        shelter_for_puppy = shelters[rand_shelter_id]
        new_puppy = get_or_create(session, Puppy,
                                  name=rand_name, gender="Male",
                                  date_of_birth=create_random_age(),
                                  picture=random.choice(PUPPY_IMAGES),
                                  shelter_id=rand_shelter_id,
                                  shelter=shelter_for_puppy,
                                  weight=create_random_weight())
        shelter_for_puppy.current_occupancy = shelter_for_puppy.current_occupancy + 1
        session.add(shelter_for_puppy)
        session.commit()

    for i, rand_name in enumerate(FEMALE_NAMES):
        shelters = get_available_shelters(session)
        rand_shelter_id = randint(0, len(shelters) - 1)
        shelter_for_puppy = shelters[rand_shelter_id]
        new_puppy = get_or_create(session, Puppy,
                                  name=rand_name, gender="Female",
                                  date_of_birth=create_random_age(),
                                  picture=random.choice(PUPPY_IMAGES),
                                  shelter_id=rand_shelter_id,
                                  shelter=shelter_for_puppy,
                                  weight=create_random_weight())
        shelter_for_puppy.current_occupancy = shelter_for_puppy.current_occupancy + 1
        session.add(shelter_for_puppy)
        session.commit()

    print "Database successfully populated!"
