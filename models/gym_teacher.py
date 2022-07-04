from teacher import SchoolTeacher

# This class inherits from parent class: SchoolTeacher
class GymTeacher(SchoolTeacher):

    # paramterized constructor: initializes class parameters name, lab_number
    def __init__(self,name, sports) -> None:

        # super() is a function call to the constructor of the parent class. 
        # (hint: check the parent class constructor definition.)
        super().__init__(name=name)
        self.sports = sports

    # function to get the lab number
    def get_sports(self):
        return self.sports
 
# z = GymTeacher('LOL', 'tennis')
# print(z.get_sports())