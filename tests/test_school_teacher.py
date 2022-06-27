from models.student import Student
from views.school_students import SchoolStudents
 
class TestSchoolTeachers:
 
    # TODO Task1.1: write test
    def test_enroll_student(self):

        schoolStudents = SchoolStudents()
        # print(type(schoolStudents))

        # variable of type Student
        first_student_in_class = Student("Maria", 20, 5)
        second_student_in_class = Student(name="Jyotsna", age=20, class_number=5)
        # first_student_in_class = Student(name="Maria", age=20, class_number=5)

        # METHOD TO TEST: enroll your first student
        schoolStudents.enroll_student(first_student_in_class)

        assert schoolStudents.enrolled_students == [first_student_in_class]

        #これは違うオブジェクトIDなので不正解
        # assert schoolStudents.enrolled_students == [Student(name="Maria", age=20, class_number=5)]

    # TODO Task1.2: write test
    def test_fetch_all_student_data(self):  
        # setup
        schoolStudents = SchoolStudents()

        # variable of type Student
        first_student_in_class = Student(name="Maria", age=20, class_number=5)
        second_student_in_class = Student(name="Jyotsna", age=20, class_number=5)

        # enroll a student
        schoolStudents.enroll_student(first_student_in_class)
        schoolStudents.enroll_student(second_student_in_class)

        # METHOD TO TEST:
        all_student_data = schoolStudents.fetch_all_student_data()

        # assertion actual result == expected result
        assert all_student_data == [first_student_in_class, second_student_in_class]

    # TODO Task1.3: write test for fetch_data_with_student_name()
    def test_fetch_data_with_student_name(self):

        schoolStudents = SchoolStudents()

        first_student_in_class = Student(name="Maria", age=20, class_number=5)
        # second_student_in_class = Student(name="Jyotsna", age=20, class_number=5)
        # third_student_in_class = Student(name="Ayumi", age=10, class_number=50)

        schoolStudents.enroll_student(first_student_in_class)
        # schoolStudents.enroll_student(second_student_in_class)
        # schoolStudents.enroll_student(third_student_in_class)

        all_student_name = schoolStudents.fetch_data_with_student_name()

        assert all_student_name == 'Maria'




