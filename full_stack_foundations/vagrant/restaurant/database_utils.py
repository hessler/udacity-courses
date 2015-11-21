"""
This module provides database utilities for the Restaurant project.
"""

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


BASE = declarative_base()
DB_URL = 'sqlite:///restaurant/restaurantmenu.db'
ENGINE = None
DB_SESSION = None
SESSION = None


def establish_session():
    """Function to establish DB session."""

    global SESSION, ENGINE, DB_SESSION
    if not SESSION:
        try:
            ENGINE = create_engine(DB_URL)
            BASE.metadata.create_all(ENGINE)
        except OperationalError, op_error:
            ENGINE = create_engine('sqlite:///restaurantmenu.db')
            BASE.metadata.create_all(ENGINE)
        BASE.metadata.bind = ENGINE

        # Setup session
        DB_SESSION = sessionmaker(bind=ENGINE)
        SESSION = DB_SESSION()
        return SESSION

# Source: http://stackoverflow.com/a/6078058/1914233
def get_or_create(session, model, **kwargs):
    """
    Function to get or create the given object.

    Args:
        session: An instance of Session
        model: The object to create and add (if not already present)
        **kwargs: Keyword arguments for the specified model object

    Returns:
        Instance of the specified object.
    """
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        # To persist new item into DB, need to add and commit!
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance
