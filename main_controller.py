from collections import abc
from models.physics_teacher import PhysicsTeacher
from models.student import Student
from models.teacher import SchoolTeacher
from views.school_students import SchoolStudents
from models.subject import SchoolSubject
from views.school_teachers import SchoolTeachers


# This file is just for our convenience for now to print and check methods and their behaviour.
# student object
# Student is data type / Class is a data type - eg. strings, Int, floats

student1 = Student(name="Jyotsna", age=29, class_number=3, grade = {'Math':
"A", "Gym": 'F'})
student2 = Student(name="Ayumi", age=19, class_number=1,  grade = {'Math':
"C", "Gym": 'C'})
student3 = Student(name="Koko", age=30, class_number=5, grade = {'Math':
"D", "Gym": 'A'} )
# access class variables
# print(student1) #Object ID で出てくる
# print(student1.age) # 29
# print(student1.class_number) # 3
# print(student1.name) # Jyotsna
# print(student1.calculate_year_of_birth())

abcSchool = SchoolStudents()
abcSchool.enroll_student(student1)
abcSchool.enroll_student(student2)
abcSchool.enroll_student(student3)
abcSchool.all_students()
abcSchool.fetch_all_student_data()
abcSchool.fetch_data_with_student_name()
print(abcSchool.enrolled_students[0])
print(student1)

# TODO: put into a view
# enroll_teachers()
physics_teacher_1 = PhysicsTeacher(name="Mia", lab_number="101")
abcSchool_teachers = SchoolTeachers()
abcSchool_teachers.enroll_teacher(physics_teacher_1)
abcSchool_teachers.all_teachers()
abcSchool_teachers.fetch_all_teacher_data()
abcSchool_teachers.fetch_data_with_teacher_name()

print("Teacher details:")
print("name:"+physics_teacher_1.name, "lab number:" + physics_teacher_1.get_lab_number())

# create a new object of type SchoolSubject and print its name
school_subject = SchoolSubject(name="Physics")
print(school_subject.name)