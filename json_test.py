import json
import jsonpickle
import pathlib

basedir = pathlib.Path(__file__).parent.resolve()

class Hero():

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

    @classmethod
    def init_from_json_str(cls, json_str):
        m = cls(None)
        m.__dict__ = json.loads(json_str)
        return m

    def temp_dump(self):
        """takes hero dict and turns it into a json file in the temp directory"""
        f = open(pathlib.Path(basedir).joinpath('static', 'temp', 'hero_pickle_storage.json'), 'w')
        stored_info = jsonpickle.encode(self)
        f.write(stored_info)
        f.close()

    def temp_pickle(self, session_id):
        with open(pathlib.Path(basedir).joinpath('static', 'temp', session_id, 'hero_pickle_storage.json'), 'w') as f:
            jsonpickle.encode(self)

def load_hero_object():
    o = open(pathlib.Path(basedir).joinpath('static', 'temp', 'hero_pickle_storage.json'), 'r')
    stored_info = o.read()

    return jsonpickle.decode(stored_info)


joe = Hero('Joe')

joe.set_power_level('Fantastic')

joe.print_hero()


# f = open('hero_storage_pickle.json', 'w')
# stored_info = jsonpickle.encode(joe)
# f.write(stored_info)
# f.close()

joe.temp_dump()

#
# o = open('hero_storage_pickle.json', 'r')
# stored_info = o.read()
#
# jack = jsonpickle.decode(stored_info)
#

jack = load_hero_object()

jack.print_hero()

print('hey')

jack.name = 'Jack'

jack.set_power_level('Weak')

jack.print_hero()

# temp_hero = grab_from_temp(session_id, 'hero_storage')
