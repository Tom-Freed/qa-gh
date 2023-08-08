from application import app
from random import choice

first_names = ['bob', 'fred', 'jim']
last_names = ['bobinson', 'fredinson', 'jiminson']

@app.route('/')
def index():
    return 'Random Name Generator'

@app.route('/generate')
def generate():
    return {'firstname':choice(first_names), 'lastname':choice(last_names)}