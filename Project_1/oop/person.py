

class Person:

    def __init__(self, firstName, middleName, lastName):
        self.first_name = firstName
        self.middle_name = middleName
        self.last_name = lastName

    def __str__(self):
        return self.first_name + ' ' + \
        self.middle_name[0] + '. ' + self.last_name