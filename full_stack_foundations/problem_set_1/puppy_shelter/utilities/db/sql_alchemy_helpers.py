"""
This module provides helper methods for interacting with SQLAlchemy.
"""

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
