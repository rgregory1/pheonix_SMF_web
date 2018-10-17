from flask import Flask, make_response, render_template, request, redirect, url_for
import datetime
from functions import *
import pathlib
from functools import wraps
import json
import jsonpickle

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

    def temp_dump(self, session_id):
        """takes hero dict and turns it into a json file in the temp directory"""
        f = open(pathlib.Path(basedir).joinpath('static', 'temp', session_id, 'hero_pickle_storage.json'), 'w')
        stored_info = jsonpickle.encode(self)
        f.write(stored_info)
        f.close()

global basedir
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
@cookie_required
def power_level_results():

    #get cookie info
    session_id = request.cookies.get('session_id')

    # get info from form
    name = request.form['heroname']
    power_level = request.form['power_level']

    # instantiate hero
    hero = Hero(name)
    hero.set_power_level(power_level)
    hero.print_hero()

    # create folder to store hero stats in
    pathlib.Path(basedir).joinpath('static', 'temp', session_id).mkdir(exist_ok=True)

    hero.temp_dump(session_id)


    if hero.power_level == 'Street-Level':
        return 'Street-Level'
    elif hero.power_level == 'Hero':
        return redirect(url_for('archetype_picker'))
    return session_id


@app.route('/archetype_picker')
@cookie_required
def archetype_picker():

    #get cookie info
    session_id = request.cookies.get('session_id')

    # temp_hero = grab_from_temp(session_id, 'hero_storage')
    # Spot = Hero.init_from_json_str(temp_hero)
    # print(Spot.name)

    hero = load_hero_object(session_id)
    return_thingy = 'archetype_picker '+ session_id + ' ' + hero.name
    return return_thingy

if __name__ == '__main__':
    # app.run()
    app.run(debug=True, host='0.0.0.0')
