import imp
from models.student import Student
from models import physics_teacher
from views.school_students import SchoolStudents
from models.subject import SchoolSubject


# This file is just for our convenience for now to print and check methods and their behaviour.
# student object
# Student is data type / Class is a data type - eg. strings, Int, floats
# student_1 = Student()
# print(student_1.age)
student = Student(name="Jyotsna", age=29, class_number=3)
# access class variables
print(student.age) # 29
print(student.class_number) # 3
print(student.name) # Jyotsna

SchoolStudents().enroll_student(student)
SchoolStudents().all_students()

# TODO: put into a view
# enroll_teachers()
physics_teacher_1 = physics_teacher.PhysicsTeacher(name="Mia", lab_number="101")

print("Teacher details:")
print("name:"+physics_teacher_1.name, "lab number:" + physics_teacher_1.get_lab_number())

# create a new object of type SchoolSubject and print its name
school_subject = SchoolSubject(name="Physics")
print(school_subject.name)