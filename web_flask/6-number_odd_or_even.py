#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """fonction that display Hello HBNB! by called /"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """fonction that display HBNB by called /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """fonction that display C and the value of <text> by called /c/<text>"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """fonction that display Python and the value of <text>
    by called /python/<text>"""
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def n_text(n):
    """fonction that display n is a number only if n is an int
    by called /number/<n>"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_html(n):
    """fonction that display a HTML page only if n is an int
    by called /number/<n>"""
    return render_template('5-number.html', num=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    choise = "odd" if n % 2 != 0 else "even"
    return render_template('6-number_odd_or_even.html', num=n, choise=choise)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)