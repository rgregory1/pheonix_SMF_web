import json

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
        self.age = 4
        self.training = 0
        self.appetite = 4
        self.speed = 6


    def add_trick(self, trick):
        self.tricks.append(trick)

    def change_name(self, name):
        self.name = name

    @classmethod
    def init_from_json_str(cls, json_str):
        m = cls(None)
        m.__dict__ = json.loads(json_str)
        return m

    def print_dog(self):
        print('------------ ', self.name, ' --------------')
        for attr, value in self.__dict__.items():
            print(attr, '=' ,value)
        print('\n\n')

    def change_stats(self, changes):
        print('beginning chagne stats method') # lets me know method is running
        for stat in changes:
            print('\nchecking for stat: ' + stat)  # test to see what is being checked
            for attr in self.__dict__.items():
                print(attr[0]) # test to see method cycle through attr's
                if stat == attr[0]:
                    print(changes[stat]) # test to insure I'm using an integer
                    attr += changes[stat]
                    break


changes = {
    "age": 1,
    "appetite": 1,
    "speed": 2
}


Fido = Dog('Fido')
print('\n\n')


Fido.print_dog()

Fido.change_stats(changes)

Fido.print_dog()

# # Json dump testing
# Fido.add_trick('roll over')
#
# print(Fido.tricks)
#
# s = json.dumps(Fido.__dict__)
#
# print(s)
#
# Spot = Dog.init_from_json_str(s)
#
# Spot.change_name('Spot')
#
# print(Spot.name)
#
# Spot.print_dog()
