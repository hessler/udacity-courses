"""
This module provides database-related items, including setup of
the DB engine and session, DB initialization, and convenience
functions.
"""

#pylint: disable=invalid-name,no-member

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///puppy_shelter/puppies.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """
    Function to initialize the application database.
    """

    # Import all modules here that might define models so that they will
    # be registered properly on the metadata. Otherwise will need to import
    # them first before calling init_db()
    Base.metadata.create_all(bind=engine)

    # Query all shelters. If none exist, we know we need to populate the DB.
    from puppy_shelter.models import Shelter
    all_shelters = db_session.query(Shelter).all()
    if len(all_shelters) < 1:
        from puppy_shelter.database_setup import populate_database
        populate_database(db_session)


def get_or_create(session, model, **kwargs):
    """
    Function to get or create the given object.

    Args:
        session: An instance of Session
        model: The object to create and add (if not already present)
        **kwargs: Keyword arguments for the specified model object

    Returns:
        Instance of the specified object.

    Source:
        http://stackoverflow.com/a/6078058/1914233
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
