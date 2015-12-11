"""
This module provides views for the Puppy Shelter project.
"""

#pylint: disable=import-error,no-member

from flask import render_template, url_for, redirect, request, flash

from puppy_shelter import app
from puppy_shelter.models import Puppy, Shelter
from puppy_shelter.database import db_session, get_or_create

# View for Shelter List
@app.route('/')
def index():
    """Function to return a page listing all shelters."""

    shelters = db_session.query(Shelter).all()
    return render_template('shelter_list.html', shelters=shelters)

# View for Shelter Information
@app.route('/shelter/<int:shelter_id>/')
def shelter_info(shelter_id):
    """Function to return a page to view a shelter's information.

    Args:
        shelter_id: ID of the shelter to view.
    """

    shelter = db_session.query(Shelter).filter_by(shelter_id=shelter_id).first()
    if not shelter:
        return render_template('404.html')
    puppies = db_session.query(Puppy).filter_by(shelter_id=shelter_id).all()
    return render_template('shelter_info.html', shelter=shelter, puppies=puppies)

# View for Adopted Puppies
@app.route('/adopted-puppies/')
def adopted_puppies():
    """Function to return a page to view a list of adopted puppies."""

    puppies = db_session.query(Puppy)\
        .filter(Puppy.shelter_id == None, Puppy.owner != '').all()
    return render_template('adopted_puppies.html', puppies=puppies)


# View for Puppy Information
@app.route('/puppy/<int:puppy_id>/')
def puppy_info(puppy_id):
    """Function to return a page to view a puppy's information.

    Args:
        puppy_id: ID of the puppy to view.
    """

    puppy = db_session.query(Puppy).filter_by(puppy_id=puppy_id).first()
    if not puppy:
        return render_template('404.html', headline_text='Puppy Not Found!')
    shelter = db_session.query(Shelter).filter_by(shelter_id=puppy.shelter_id).first()
    return render_template('puppy_info.html', puppy=puppy, shelter=shelter)

# View for Adding a New Puppy
@app.route('/shelter/<int:shelter_id>/new_puppy/', methods=['GET', 'POST'])
def new_puppy(shelter_id):
    """Function to return a page to add a new puppy.

    Args:
        shelter_id: ID of the shelter where the new puppy will live.
    """

    shelter = db_session.query(Shelter).filter_by(shelter_id=shelter_id).first()
    if not shelter:
        redirect(url_for('shelter_info', shelter_id=shelter.shelter_id))

    if request.method == 'POST':
        puppy = get_or_create(db_session, Puppy,
                              name=request.form['name'],
                              picture=request.form['picture'],
                              gender=request.form['gender'],
                              weight=request.form['weight'],
                              shelter_id=shelter_id)
        shelter.current_occupancy = shelter.current_occupancy + 1
        db_session.add(shelter)
        db_session.commit()
        flash("New puppy {} created!".format(puppy.name))
        return redirect(url_for('shelter_info', shelter_id=shelter_id))
    else:
        return render_template('new_puppy.html', shelter=shelter)

# View for Editing a Puppy
@app.route('/puppy/<int:puppy_id>/edit/', methods=['GET', 'POST'])
def edit_puppy(puppy_id):
    """Function to return a page to edit a puppy.

    Args:
        puppy_id: ID of the puppy to edit.
    """

    puppy = db_session.query(Puppy)\
        .filter_by(puppy_id=puppy_id).first()
    if not puppy:
        return render_template('404.html', headline_text='Puppy Not Found!')

    # Get all available shelters. This is used in the template for
    # populating the dropdown list of available shelters that have
    # capacity available.
    shelters = db_session.query(Shelter)\
        .filter(Shelter.current_occupancy < Shelter.maximum_capacity).all()

    if request.method == 'POST':
        puppy.name = request.form['name']
        puppy.picture = request.form['picture']
        puppy.gender = request.form['gender']
        puppy.weight = request.form['weight']

        # The same form is used, but depending on the adoption status,
        # it will sometimes have shelter_id info, and sometimes not.
        if 'original_shelter_id' in request.form:
            original_shelter_id = request.form['original_shelter_id']
            shelter_id = request.form['shelter_id']

            # If form shelter id doesn't match puppy's original shelter id,
            # update both the shelter's and original shelter's occupancy.
            if shelter_id != original_shelter_id:
                puppy.shelter_id = shelter_id
                shelter = db_session.query(Shelter)\
                    .filter_by(shelter_id=shelter_id).first()
                original_shelter = db_session.query(Shelter)\
                    .filter_by(shelter_id=original_shelter_id).first()
                if not shelter or not original_shelter:
                    return render_template('404.html', headline_text='Shelter Not Found!')
                shelter.current_occupancy = shelter.current_occupancy + 1
                original_shelter.current_occupancy = original_shelter.current_occupancy - 1
                db_session.add_all([shelter, original_shelter])
                db_session.commit()
        else:
            puppy.owner = request.form['owner']

        db_session.add(puppy)
        db_session.commit()
        flash("{} updated!".format(puppy.name))
        return redirect(url_for('puppy_info', puppy_id=puppy_id))
    else:
        return render_template('edit_puppy.html', puppy=puppy,
                               shelter=puppy.shelter, shelters=shelters)


# View for Adopting a Puppy
@app.route('/puppy/<int:puppy_id>/adopt/', methods=['GET', 'POST'])
def adopt_puppy(puppy_id):
    """Function to return a page to adopt a puppy.

    Args:
        puppy_id: ID of the puppy to adopt.
    """

    puppy = db_session.query(Puppy)\
        .filter_by(puppy_id=puppy_id).first()
    if not puppy:
        return render_template('404.html', headline_text='Puppy Not Found!')

    if request.method == 'POST':
        # Remove shelter_id and shelter from Puppy object, and add owner.
        # Update Shelter's occupancy. Commit both objects to DB session.
        shelter = db_session.query(Shelter)\
            .filter_by(shelter_id=puppy.shelter_id).first()
        if not shelter:
            return render_template('404.html', headline_text='Shelter Not Found!')
        puppy.owner = request.form['name']
        puppy.shelter_id = ''
        puppy.shelter = None
        shelter.current_occupancy = shelter.current_occupancy - 1
        db_session.add_all([puppy, shelter])
        db_session.commit()
        flash("{} has been adopted!".format(puppy.name))
        return redirect(url_for('puppy_info', puppy_id=puppy_id))
    else:
        return render_template('adopt_puppy.html', puppy=puppy, shelter=puppy.shelter)
