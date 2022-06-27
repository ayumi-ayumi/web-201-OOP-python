from models.student import Student
from models.teacher import SchoolTeacher
from views.school_students import SchoolStudents
from views.school_teachers import SchoolTeachers
 
class TestSchoolTeachers:
 
    # TODO Task1.1: write test
    def test_enroll_teacher(self):

        schoolTeachers = SchoolTeachers()

        # variable of type Student
        first_teacher = SchoolTeacher("Ayumi")
        # second_teacher = SchoolTeacher("Emily")

        # METHOD TO TEST: enroll first teacher
        schoolTeachers.enroll_teacher(first_teacher)

        assert schoolTeachers.enrolled_teachers == [first_teacher]

        #これは違うオブジェクトIDなので不正解
        # assert schoolStudents.enrolled_students == [Student(name="Maria", age=20, class_number=5)]

    def test_fetch_all_teacher_data(self):  
        schoolTeachers = SchoolTeachers()

        first_teacher = SchoolTeacher("Ayumi")
        second_teacher = SchoolTeacher("Emily")

        schoolTeachers.enroll_teacher(first_teacher)
        schoolTeachers.enroll_teacher(second_teacher)

        all_teacher_data = schoolTeachers.fetch_all_teacher_data()

        # assertion actual result == expected result
        assert all_teacher_data == [first_teacher, second_teacher]

    # TODO Task1.3: write test for fetch_data_with_student_name()
    def test_fetch_data_with_teacher_name(self):

        schoolTeachers = SchoolTeachers()

        first_teacher = SchoolTeacher("Ayumi")

        schoolTeachers.enroll_teacher(first_teacher)

        all_student_name = schoolTeachers.fetch_data_with_teacher_name()

        assert all_student_name == 'Ayumi'




