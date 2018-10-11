import json
import jsonpickle

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

    @classmethod
    def init_from_json_str(cls, json_str):
        m = cls()
        m.__dict__ = json.loads(json_str)
        return m

Fido = Dog('Fido')
print('\n\n')
print(Fido.name)

Fido.add_trick('roll over')
print(Fido.tricks)
#
# s = json.dumps(Fido.__dict__)
# print('\n\n')
# print(s)
# print('\n\n')
#
# Spot = Dog(init_from_json_str(s))
# # Spot = Dog()
# # Spot.init_from_json_str(s)
#
# print(Spot.name)

s = jsonpickle.encode(Fido)

print(s)

Spot = jsonpickle.decode(s)

Spot.add_trick('shake hands')

print(Spot.tricks)
