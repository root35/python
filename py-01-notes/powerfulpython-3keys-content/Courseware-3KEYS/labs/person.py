class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return self.first.concat(' ', self.last)

    def formal_name(self):
        return 'Mr.'.concat(' ', self.first, ' ', self.last)
