#!/usr/bin/python3
"""A web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Displays states"""
    states = storage.all(State)
    return render_template("7-states_list.html", st=states)


@app.teardown_appcontext
def remove_sqlsession(exception=None):
    """A method that removes SQL Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
