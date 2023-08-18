#!/usr/bin/python3
"""Web App with Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Get cities by states"""
    list_states = storage.all(State)
    list_cities = storage.all(City)
    return render_template('8-cities_by_states.html', cities=list_cities,
                           states=list_states)


@app.teardown_appcontext
def remove_sqlsession(exception=None):
    """A method that removes SQL Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
