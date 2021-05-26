class Pet(object):
    '''
    >>> rover = Pet('rover')
    >>> rover.speak()
    My name is rover and I have 1 pets.
    >>> spot = Pet('spot')
    >>> rover.speak()
    My name is rover and I have 2 pets.
    >>> spot.speak()
    My name is spot and I have 2 pets.
    '''
    num_pets = 0

    def __init__(self, name):
        self.name = name
        Pet.num_pets += 1

    def speak(self):
        print(f'My name is {self.name} and I have {Pet.num_pets} pets.')
