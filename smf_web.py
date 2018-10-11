import json
# import jsonpickle

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

    @classmethod
    def init_from_json_str(cls, json_str):
        m = cls(None)
        m.__dict__ = json.loads(json_str)
        return m

    def print_dog(self):
        for attr, value in self.__dict__.items():
            print(attr, '=' ,value)

Fido = Dog('Fido')
print('\n\n')
print(Fido.name)

Fido.add_trick('roll over')
print(Fido.tricks)

s = json.dumps(Fido.__dict__)
print('\n\n')
print(s)
print('\n\n')

Spot = Dog.init_from_json_str(s)
# Spot = Dog()
# Spot.init_from_json_str(s)

print(Spot.name)

print(Spot.print_dog())

print(Spot)
# s = jsonpickle.encode(Fido)
#
# print(s)
#
# Spot = jsonpickle.decode(s)
#
# Spot.add_trick('shake hands')
#
# print(Spot.tricks)
