from .teacher import SchoolTeacher

# This class inherits from parent class: SchoolTeacher
class PhysicsTeacher(SchoolTeacher):

    # paramterized constructor: initializes class parameters name, lab_number
    def __init__(self,name, lab_number) -> None:

        # super() is a function call to the constructor of the parent class. 
        # (hint: check the parent class constructor definition.)
        super().__init__(name=name)
        self.lab_number = lab_number

    # function to get the lab number
    def get_lab_number(self):
        return self.lab_number

# x = PhysicsTeacher('Amy', 23)
# print(x.name)