
from models.subject import SchoolSubject


class SchoolSubjects(SchoolSubject):

    def __init__(self):
        self.enlisted_subject = []

    def enlist_a_subject(self, subject):
        self.enlisted_subject.append(subject)
    
    def view_all_subjects(self):
        return self.enlisted_subject

    def view_subject_syllabus(self):
        for each_subject in self.enlisted_subject:
            print("Name :" + each_subject.name)
            print("Syllabus :" + each_subject.syllabus)