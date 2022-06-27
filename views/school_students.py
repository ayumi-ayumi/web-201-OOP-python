# This class is used to store/maintain the collection of students in the school.


from models.student import Student


class SchoolStudents(Student):

    # constructor for the class
    # initilizes the class variable enroll_students to an empty list
    def __init__(self):
        self.enrolled_students = []

    # func to add a student to the list of enrolled students
    def enroll_student(self, student):
        self.enrolled_students.append(student)
    
    #  func to print out the details of all enrolled students
    def all_students(self):
        for each_student in self.enrolled_students:
            print("Name :" + each_student.name)
            print("Age :" + each_student.age)
            print("Class number :" + each_student.class_number)
            print("Grade :" + each_student.grade)
            
    # TODO Task1.1:implement a func to get all students' data
    def fetch_all_student_data(self):
        return self.enrolled_students

    # TODO Task1.2:implement a function get student with name
    def fetch_data_with_student_name(self):
        for each_student in self.enrolled_students:
            return each_student.name

