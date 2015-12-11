"""
This module provides the handling of web server logic.
"""

#pylint: disable=invalid-name,anomalous-backslash-in-string, global-statement

import cgi
import re
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from restaurant.database_utils import establish_session, get_or_create
from restaurant.models import Restaurant

SESSION = None
CONTENT_TYPE = "Content-type"
CT_TEXT_HTML = "text/html"
MULTI_FORM_DATA = "multipart/form-data"
RE_PATTERN_EDIT = "\/(restaurants)\/[0-9]+\/(edit)"
RE_PATTERN_DELETE = "\/(restaurants)\/[0-9]+\/(delete)"

class WebServerHandler(BaseHTTPRequestHandler):
    """Method for handling web server events."""

    # do_GET overrides method in base handler class
    def do_GET(self):
        """Method to handle GET requests."""

        global SESSION
        if not SESSION:
            SESSION = establish_session()
        try:
            if self.path.endswith("/"):
                output = """<a href=\"restaurants\" title=\"Restaurants\">
                    View Restaurants</a>"""
                base_response(self, "Welcome", output)

            if self.path.endswith("/restaurants"):
                output = """<div class='columns medium-12'>&nbsp;</div>
                    <div class='columns medium-12'>
                    <a href='/restaurants/new' class='button round'
                        title='Add Restaurant'>Add Restaurant +</a>
                    </div>"""
                output += all_restaurants_markup()
                base_response(self, "Restaurants", output)
                return

            if self.path.endswith("/restaurants/new"):
                output = """<h1>Add a New Restaurant</h1>
                    <form method='POST' enctype='{}'
                        action='/restaurants/new'>
                    <input type='text' name='new_restaurant'
                        placeholder='Restaurant Name'/>
                    <input type='submit' class='button round'
                        name='submit' value='Submit'/>
                    </form>""".format(MULTI_FORM_DATA)
                base_response(self, "Add New Restaurant", output)
                return

            if re.search(RE_PATTERN_EDIT, self.path) is not None:
                r_id = self.path.split('/')[2]
                restaurant = SESSION.query(Restaurant)\
                    .filter_by(restaurant_id='{}'.format(r_id)).first()
                output = """<div class='restaurant columns medium-12'>"""
                if restaurant:
                    output += """<h1>Editing {0}</h1>
                        <form method='POST' enctype='{1}'
                            action='/restaurants/{2}/edit'>
                        <input type='hidden' name='restaurant_id'
                            value='{2}'/>
                        <input type='text' name='restaurant_name'
                            placeholder='Restaurant Name' value='{0}'/>
                        <input type='submit' class='button round'
                            name='submit' value='Rename'/>
                        <a href='/restaurants' class='button round secondary'
                            title='Cancel'>Cancel</a>
                        </form>
                        """.format(restaurant.name, MULTI_FORM_DATA, r_id)
                else:
                    output += """<h1>Restaurant not found.</h1>
                        <p>
                        <a href='/restaurants' class='button round'
                            title='Back to Restaurants List'>
                            Back to Restaurants List</a>
                        </p>"""
                output += """</div>"""
                base_response(self, "Edit Restaurant", output)
                return

            if re.search(RE_PATTERN_DELETE, self.path) is not None:
                r_id = self.path.split('/')[2]
                restaurant = SESSION.query(Restaurant)\
                    .filter_by(restaurant_id='{}'.format(r_id)).first()
                output = """<div class='restaurant columns medium-12'>"""
                if restaurant:
                    output += """<h1>Are you sure you want to delete {0}?</h1>
                        <form method='POST' enctype='{1}'
                            action='/restaurants/{2}/delete'>
                        <input type='hidden' name='restaurant_id' value='{2}'/>
                        <input type='submit' class='button round'
                            name='submit' value='Delete'/>
                        <a href='/restaurants'
                            class='button round secondary'
                            title='Cancel'>Cancel</a>
                        </form>
                    """.format(restaurant.name, MULTI_FORM_DATA, r_id)
                else:
                    output += """<h1>Restaurant not found.</h1>
                        <p>
                        <a href='/restaurants' class='button round'
                            title='Back to Restaurants List'>
                            Back to Restaurants List</a>
                        </p>"""
                output += """</div>"""
                base_response(self, "Delete Restaurant", output)
                return

        except IOError:
            self.send_error(404, "File Not Found: {}".format(self.path))

    def do_POST(self):
        """Method to handle POST requests."""

        global SESSION
        if not SESSION:
            SESSION = establish_session()
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
                if ctype == "multipart/form-data":
                    form_fields = cgi.parse_multipart(self.rfile, pdict)
                    new_restaurant = form_fields.get("new_restaurant")[0]
                    restaurant = get_or_create(SESSION, Restaurant, name=new_restaurant)
                    base_post_response(self, "Restaurants",\
                        all_restaurants_markup(), "/restaurants")

            if re.search(RE_PATTERN_EDIT, self.path) is not None:
                ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
                if ctype == "multipart/form-data":
                    form_fields = cgi.parse_multipart(self.rfile, pdict)
                    r_name = form_fields.get("restaurant_name")[0]
                    r_id = form_fields.get("restaurant_id")[0]
                    restaurant = SESSION.query(Restaurant)\
                        .filter_by(restaurant_id='{}'.format(r_id)).first()
                    if restaurant:
                        restaurant.name = r_name
                        SESSION.add(restaurant)
                        SESSION.commit()
                    base_post_response(self, "Restaurants",\
                        all_restaurants_markup(), "/restaurants")

            if re.search(RE_PATTERN_DELETE, self.path) is not None:
                ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
                if ctype == "multipart/form-data":
                    form_fields = cgi.parse_multipart(self.rfile, pdict)
                    r_id = form_fields.get("restaurant_id")[0]
                    restaurant = SESSION.query(Restaurant)\
                        .filter_by(restaurant_id='{}'.format(r_id)).first()
                    if restaurant:
                        SESSION.delete(restaurant)
                        SESSION.commit()
                    base_post_response(self, "Restaurants",\
                        all_restaurants_markup(), "/restaurants")

        except IOError:
            self.send_error(404, "File Not Found: {}".format(self.path))


def base_response(self, page_title="", output_content=""):
    """Convenience function to return base response with status code 200.

    Args:
        page_title: Optional page title to include in the returned HTML.
        output_content: Optional content to include in the returned HTML.
    """

    self.send_response(200)
    self.send_header(CONTENT_TYPE, CT_TEXT_HTML)
    self.end_headers()
    output = html_wrapper_open(page_title)
    output += output_content
    output += html_wrapper_close()
    self.wfile.write(output)

def base_post_response(self, page_title="", output_content="", redirect_location=""):
    """Convenience function to return base response with status code 301.

    Args:
        page_title: Optional page title to include in the returned HTML.
        output_content: Optional content to include in the returned HTML.
    """

    self.send_response(301)
    self.send_header(CONTENT_TYPE, CT_TEXT_HTML)
    if redirect_location is not "":
        self.send_header("Location", redirect_location)
    self.end_headers()
    output = html_wrapper_open(page_title)
    output += output_content
    output += html_wrapper_close()
    self.wfile.write(output)

def css_styles():
    """Function to return CSS styles for HTML page."""

    return """
        .restaurant {
            margin: 1.5rem 0;
        }
        .restaurant h1 {
            margin: 0 0 0.75rem 0;
        }
        .restaurant a.button {
            margin: 0.125rem;
        """

def html_wrapper_open(page_title=""):
    """Function to return base HTML for the beginning of the page.

    Args:
        page_title: Optional page title to include in the returned HTML.
    """

    return """<html>
        <head>
        <title>{}</title>
        <link rel='stylesheet'href='https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css'>
        <style type='text/css'>
        {}
        </style>
        </head>
        <body>
        <div class='row'>""".format(page_title, css_styles())

def html_wrapper_close():
    """Function to return base HTML for the end of the page."""

    return "</div></body></html>"

def all_restaurants_markup():
    """Convenience function to return HTML output of all Restaurants."""

    global SESSION
    if not SESSION:
        SESSION = establish_session()
    output = ""
    all_restaurants = SESSION.query(Restaurant).all()
    for restaurant in all_restaurants:
        output += """<div class='restaurant columns medium-12'>
            <h1>{0}</h1>
            <a href='/restaurants/{1}/edit'
                title='Edit' class='button round'>Edit</a>
            <a href='/restaurants/{1}/delete'
                title='Delete' class='button round'>Delete</a>
            </div>""".format(restaurant.name, restaurant.restaurant_id)
    return output



def main():
    """Main function that runs by default when web server is called."""

    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web server running on port {}. Press Ctrl+C to quit.".format(port)
        server.serve_forever()
    except KeyboardInterrupt:
        print " Stopping web server..."
        server.socket.close()


# Uncomment if we want to run the main function automatically.
# For now, since this file is not meant to be used, it's commented out.
# In place of triggering this file, use 'restaurant/project.py'.
#if __name__ == '__main__':
#    main()
