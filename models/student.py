class Student:

    # this is all defalt 書かなくてもOK
    # def __init__(self) -> None:
    #     self.age = 0
    #     self.name = ""
    #     self.grade = {}
    #     pass

    # initialize class data/variables
    def __init__(self, name, age, class_number):
        self.name = name
        self.age = age
        self.class_number = class_number
        self.grade = {}

    def calculate_dob(self, current_year):
        pass

