import string


class SchoolTeacher:

    def __init__(self):
        pass
    
    # parameterized constructor
    def __init__(self, name):
        self.name = name

    def get_name(self) -> string:
        return self.name