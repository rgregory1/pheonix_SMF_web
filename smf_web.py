from flask import Flask, make_response, render_template, request
import datetime
from functions import *
import pathlib

app = Flask(__name__)

class Hero:

    def __init__(self, name):
        self.name = name
        self.notes = []
        self.move = 0
        self.body_points = 0
        self.psych_points = 0
        self.power_level = None

    def set_power_level(self, power_level):
        self.power_level = power_level

    def print_hero(self):
        print('\n\n------------ ', self.name, ' --------------')
        for attr, value in self.__dict__.items():
            print(attr, '=' ,value)
        print('\n\n')

basedir = pathlib.Path(__file__).parent.resolve()

def cookie_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'session_id' not in request.cookies:
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def start_page():
    ''' beginning page in process, start a folder and get initial choices '''

    # get timestamp and convert to string so it can be used to save data to same folder
    temp_timestamp = str(datetime.datetime.now())
    timestamp = simplify_timestamp(temp_timestamp)

    # list of power levels to choose from
    power_level_list = ['Street-Level', 'Hero', 'Super', 'Powerhouse']

    # create response and set cookie
    resp = make_response(render_template('home.html', timestamp=timestamp, power_level_list=power_level_list))
    resp.set_cookie('session_id', timestamp)

    return resp

@app.route('/power_level_results', methods=['POST'])
def power_level_results():

    # get info from form
    name = request.form['heroname']
    power_level = request.form['power_level']

    # instantiate hero
    hero = Hero(name)
    hero.set_power_level(power_level)
    hero.print_hero()
    return 'hello'

if __name__ == '__main__':
    # app.run()
    app.run(debug=True, host='0.0.0.0')
