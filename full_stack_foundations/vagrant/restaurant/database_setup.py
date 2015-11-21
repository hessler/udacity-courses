"""
This module provides database setup and configuration.
"""

from database_utils import establish_session
from models import Restaurant, MenuItem

SESSION = None

def create_data():
    """Function to create and set up DB and populate with data."""

    global SESSION
    SESSION = establish_session()

    # Query for restaurant list. If none exist, create via prefab data.
    all_restaurants = SESSION.query(Restaurant).all()
    if len(all_restaurants) < 1:
        import prefab_db_data
        prefab_db_data.create_all_the_things(SESSION)
        all_restaurants = SESSION.query(Restaurant).all()

def update_ub_veggie_burger():
    """Function to update the price of the Veggie Burger at Urban Burger."""

    if not SESSION:
        create_data()

    # Reset price of Urban Burger's Veggie Burger
    urban_burger = SESSION.query(Restaurant).filter_by(
        name="Urban Burger"
    ).first() or None

    if urban_burger:
        urban_burger_veggie_burger = SESSION.query(MenuItem).filter_by(
            name="Veggie Burger", restaurant=urban_burger
        ).first() or None
        urban_burger_veggie_burger.price = "$2.99"
        SESSION.add(urban_burger_veggie_burger)
        SESSION.commit()
        print "Urban Burger's Veggie Burger price updated."

def update_all_veggie_burger_prices():
    """Function to update the price of all Veggie Burgers."""

    if not SESSION:
        create_data()

    # Reset price of Urban Burger's Veggie Burger
    veggie_burgers = SESSION.query(MenuItem).filter_by(
        name="Veggie Burger"
    )
    # Reset other restaurant's veggie burger prices
    for burger in veggie_burgers:
        if burger.price != "$2.99":
            burger.price = "$2.99"
            SESSION.add(burger)
            SESSION.commit()
    print "All Veggie Burger prices updated."

def delete_spinach_ice_cream():
    """Function to delete Spinach Ice Cream from Auntie Ann's menu."""

    if not SESSION:
        create_data()

    # Delete Spinach Ice Cream from Auntie Ann's Diner menu
    auntie_anns = SESSION.query(Restaurant).filter_by(
        name="Auntie Ann\'s Diner"
    ).first() or None
    if auntie_anns:
        spinach_ice_cream = SESSION.query(MenuItem).filter_by(
            name="Spinach Ice Cream", restaurant=auntie_anns
        ).first() or None
        if spinach_ice_cream:
            SESSION.delete(spinach_ice_cream)
            SESSION.commit()
        spinach_ice_cream = SESSION.query(MenuItem).filter_by(
            name="Spinach Ice Cream", restaurant=auntie_anns
        ).first() or None
        print "Spinach Ice Cream removed from menu."

def print_all_restaurants():
    """Function to query and print out all restaurant names."""

    if not SESSION:
        create_data()

    all_restaurants = SESSION.query(Restaurant).all()
    print "Restaurants:"
    for restaurant in all_restaurants:
        print "  - {}".format(restaurant.name)


# Run function to create data
if __name__ == '__main__':
    create_data()
