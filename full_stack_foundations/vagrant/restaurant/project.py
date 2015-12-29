"""
This module provides logic for returning views for the Restaurant project.
"""

#pylint: disable=relative-import,invalid-name,import-error

from flask import Flask, render_template, url_for
from flask import redirect, request, flash, jsonify
from database_utils import establish_session, get_or_create
from models import Restaurant, MenuItem

SESSION = establish_session()

# Create instance of Flask class
app = Flask(__name__)

# Including '/' so the main directory gets a valid response, not a 404.
# Using <> makes dynamic URLs possible, substituting var name as part of URL.
# Ex: "path/<type:var_name>/path" -- where "type" can be int, string, or path.
@app.route('/')
@app.route('/restaurants/')
def all_restaurants():
    """Function to return full list of Restaurants."""

    restaurants = SESSION.query(Restaurant).all()
    return render_template('restaurant_list.html', restaurants=restaurants)


@app.route('/restaurant/new/', methods=['GET', 'POST'])
def new_restaurant():
    """Function to return a page to add a new restaurant."""

    if request.method == 'POST':
        new_item = get_or_create(SESSION, Restaurant,
                                 name=request.form['name'])
        flash("New restaurant created: {}".format(new_item.name))
        return redirect(url_for('all_restaurants'))
    else:
        return render_template('new_restaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    """Function to return a page to edit a restaurant.

    Args:
        restaurant_id: ID of the restaurant to edit.
    """

    restaurant = SESSION.query(Restaurant)\
        .filter_by(restaurant_id=restaurant_id).one()
    if not restaurant:
        return redirect(url_for('all_restaurants'))
    if request.method == 'POST':
        restaurant.name = request.form['name']
        SESSION.add(restaurant)
        SESSION.commit()
        flash("{} updated!".format(restaurant.name))
        return redirect(url_for('restaurant_menu',
                                restaurant_id=restaurant_id))
    else:
        return render_template('edit_restaurant.html',
                               restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):
    """Function to return a page to delete a restaurant.

    Args:
        restaurant_id: ID of the restaurant to delete.
    """

    restaurant = SESSION.query(Restaurant)\
        .filter_by(restaurant_id=restaurant_id).one()
    if not restaurant:
        return redirect(url_for('all_restaurants'))
    if request.method == 'POST':
        SESSION.delete(restaurant)
        SESSION.commit()
        flash("{} deleted.".format(restaurant.name))
        return redirect(url_for('all_restaurants'))
    else:
        return render_template('delete_restaurant.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def restaurant_menu(restaurant_id):
    """Function to return the menu for the specified restaurant.

    Args:
        restaurant_id: ID of the restaurant whose menu to retrieve.
    """

    restaurant = SESSION.query(Restaurant)\
        .filter_by(restaurant_id=restaurant_id).one()
    if not restaurant:
        return "Restaurant not found."
    menu_items = SESSION.query(MenuItem)\
        .filter_by(restaurant_id=restaurant_id)\
        .order_by(MenuItem.course)
    return render_template('menu.html', restaurant=restaurant,
                           menu_items=menu_items)


@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    """Function to return a page to add a new menu item.

    Args:
        restaurant_id: ID of the restaurant where the new menu item
                       will be created.
    """

    if request.method == 'POST':
        new_item = get_or_create(SESSION, MenuItem,
                                 name=request.form['name'],
                                 course=request.form['course'],
                                 price=request.form['price'],
                                 description=request.form['description'],
                                 restaurant_id=restaurant_id)
        flash("New menu item {} created!".format(new_item.name))
        return redirect(url_for('restaurant_menu',
                                restaurant_id=restaurant_id))
    else:
        restaurant = SESSION.query(Restaurant)\
            .filter_by(restaurant_id=restaurant_id).one()
        if not restaurant:
            redirect(url_for('restaurant_menu', restaurant_id=restaurant_id))
        return render_template('new_menu_item.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/edit/',
           methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_item_id):
    """Function to return a page to edit a menu item.

    Args:
        restaurant_id: ID of the restaurant.
        menu_item_id: ID of the menu item to edit.
    """

    restaurant = SESSION.query(Restaurant)\
        .filter_by(restaurant_id=restaurant_id).one()
    edit_item = SESSION.query(MenuItem)\
        .filter_by(restaurant_id=restaurant_id, menu_item_id=menu_item_id)\
        .first()
    if not edit_item or not restaurant:
        return redirect(url_for('restaurant_menu',
                                restaurant_id=restaurant_id))
    if request.method == 'POST':
        edit_item.name = request.form['name']
        edit_item.course = request.form['course']
        edit_item.price = request.form['price']
        edit_item.description = request.form['description']
        SESSION.add(edit_item)
        SESSION.commit()
        flash("Menu item {} updated!".format(edit_item.name))
        return redirect(url_for('restaurant_menu',
                                restaurant_id=restaurant_id))
    else:
        restaurant = SESSION.query(Restaurant)\
            .filter_by(restaurant_id=restaurant_id).one()
        if not restaurant:
            return "Restaurant not found."
        menu_item = SESSION.query(MenuItem)\
            .filter_by(menu_item_id=menu_item_id).one()
        if not menu_item:
            return "Menu Item not found."
        return render_template('edit_menu_item.html',
                               restaurant=restaurant, menu_item=menu_item)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/delete/',
           methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_item_id):
    """Function to return a page to delete a menu item.

    Args:
        restaurant_id: ID of the restaurant.
        menu_item_id: ID of the menu item to delete.
    """

    restaurant = SESSION.query(Restaurant)\
        .filter_by(restaurant_id=restaurant_id).one()
    delete_item = SESSION.query(MenuItem)\
        .filter_by(restaurant_id=restaurant_id, menu_item_id=menu_item_id)\
        .first()
    if not delete_item or not restaurant:
        return redirect(url_for('restaurant_menu',
                                restaurant_id=restaurant_id))
    if request.method == 'POST':
        SESSION.delete(delete_item)
        SESSION.commit()
        flash("Menu item {} deleted.".format(delete_item.name))
        return redirect(url_for('restaurant_menu',
                                restaurant_id=restaurant_id))
    else:
        return render_template('delete_menu_item.html',\
            restaurant=restaurant, menu_item=delete_item)


# API Endpoints (GET Request)
@app.route('/restaurants/json/')
def restaurants_json():
    """Function to return a JSON list of restaurants."""

    restaurants = SESSION.query(Restaurant).all()
    return jsonify(Restaurants=[item.serialize for item in restaurants])

@app.route('/restaurant/<int:restaurant_id>/json/')
@app.route('/restaurant/<int:restaurant_id>/menu/json/')
def restaurant_menu_json(restaurant_id):
    """Function to return a menu (in JSON) for the specified restaurant.

    Args:
        restaurant_id: ID of the restaurant whose menu to retrieve.
    """

    restaurant = SESSION.query(Restaurant)\
        .filter_by(restaurant_id=restaurant_id).one()
    if not restaurant:
        return {'error': 'Restaurant not found.'}
    menu_items = SESSION.query(MenuItem)\
        .filter_by(restaurant_id=restaurant_id)\
        .order_by(MenuItem.course)
    return jsonify(MenuItems=[item.serialize for item in menu_items])

@app.route('/restaurant/<int:restaurant_id>/<int:menu_item_id>/json/')
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/json/')
def menu_item_json(restaurant_id, menu_item_id):
    """Function to return a menu item (in JSON).

    Args:
        restaurant_id: ID of the restaurant.
        menu_item_id: ID of the menu item to retrieve.
    """

    restaurant = SESSION.query(Restaurant)\
        .filter_by(restaurant_id=restaurant_id).one()
    menu_item = SESSION.query(MenuItem)\
        .filter_by(restaurant_id=restaurant_id, menu_item_id=menu_item_id)\
        .first()
    if not restaurant:
        return {'error': 'Invalid restaurant id.'}
    if not menu_item:
        return {'error': 'Invalid menu item id.'}
    return jsonify(MenuItem=menu_item.serialize)


if __name__ == '__main__':
    app.secret_key = '$up3r$3cr3tK3y'
    app.debug = True
    # Run the local server
    app.run(host='0.0.0.0', port=5000)
