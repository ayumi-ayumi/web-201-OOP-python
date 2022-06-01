from models.teacher import SchoolTeacher

class PhysicsTeacher(SchoolTeacher):
    def __init__(self,name, lab_number) -> None:
        super().__init__(name=name)
        self.lab_number = lab_number

    def get_lab_number(self):
        return self.lab_number