from person import Person

class Student(Person):

    def __init__(self, firstName, middleName, lastName, studentID, major):
        # Constructor chaining
        super().__init__(firstName, middleName, lastName)
        # set subclass properties
        self.student_id = studentID
        self.major = major
        

