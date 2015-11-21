"""
This module provides pre-fab data for puppy and shelter items
that can be added to the database for testing.
"""

import datetime
import random
from random import randint

from puppies import BASE, Shelter, Puppy
from utilities.db.sql_alchemy_helpers import get_or_create

ALL_SHELTERS = []

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
    "http://pixabay.com/get/da0c8c7e4aa09ba3a353/1433170694/dog-785193_1280.jpg?direct",
    "http://pixabay.com/get/6540c0052781e8d21783/1433170742/dog-280332_1280.jpg?direct",
    "http://pixabay.com/get/8f62ce526ed56cd16e57/1433170768/pug-690566_1280.jpg?direct",
    "http://pixabay.com/get/be6ebb661e44f929e04e/1433170798/pet-423398_1280.jpg?direct",
    "http://pixabay.com/static/uploads/photo/2010/12/13/10/20/beagle-puppy-2681_640.jpg",
    "http://pixabay.com/get/4b1799cb4e3f03684b69/1433170894/dog-589002_1280.jpg?direct",
    "http://pixabay.com/get/3157a0395f9959b7a000/1433170921/puppy-384647_1280.jpg?direct",
    "http://pixabay.com/get/2a11ff73f38324166ac6/1433170950/puppy-742620_1280.jpg?direct",
    "http://pixabay.com/get/7dcd78e779f8110ca876/1433170979/dog-710013_1280.jpg?direct",
    "http://pixabay.com/get/31d494632fa1c64a7225/1433171005/dog-668940_1280.jpg?direct"
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

def create_shelters(session):
    """Function to create Shelter objects."""

    shelter_1 = get_or_create(session, Shelter,
                              name="Oakland Animal Services",
                              address="1101 29th Ave",
                              city="Oakland",
                              state="California",
                              zip_code="94601",
                              website="oaklandanimalservices.org")

    shelter_2 = get_or_create(session, Shelter,
                              name="San Francisco SPCA Mission "\
                              "Adoption Center",
                              address="250 Florida St",
                              city="San Francisco",
                              state="California",
                              zip_code="94103",
                              website="sfspca.org")

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
                              website="hsalameda.org")

    shelter_5 = get_or_create(session, Shelter,
                              name="Palo Alto Humane Society",
                              address="1149 Chestnut St.",
                              city="Menlo Park",
                              state="California",
                              zip_code="94025",
                              website="paloaltohumane.org")

    ALL_SHELTERS.extend(
        [shelter_1, shelter_2, shelter_3, shelter_4, shelter_5]
    )


def create_all_the_things(session):
    """Function to create Shelter and Puppy objects."""

    create_shelters(session)

    for i, rand_name in enumerate(MALE_NAMES):
        rand_shelter_id = randint(0, 4)
        new_puppy = get_or_create(session, Puppy,
                                  name=rand_name, gender="Male",
                                  date_of_birth=create_random_age(),
                                  picture=random.choice(PUPPY_IMAGES),
                                  shelter_id=rand_shelter_id,
                                  shelter=ALL_SHELTERS[rand_shelter_id],
                                  weight=create_random_weight())

    for i, rand_name in enumerate(FEMALE_NAMES):
        rand_shelter_id = randint(0, 4)
        new_puppy = get_or_create(session, Puppy,
                                  name=rand_name, gender="Female",
                                  date_of_birth=create_random_age(),
                                  picture=random.choice(PUPPY_IMAGES),
                                  shelter_id=rand_shelter_id,
                                  shelter=ALL_SHELTERS[rand_shelter_id],
                                  weight=create_random_weight())
