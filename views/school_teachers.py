
#TODO Task2.2: This class is used to store/maintain the collection of teachers in the school.


from models.teacher import SchoolTeacher


class SchoolTeachers(SchoolTeacher):

    # constructor for the class
    # initilizes the class variable enrolled_teachers to an empty list
    def __init__(self):
        self.enrolled_teachers = []

    # func to add a teacher to the list of enrolled teachers
    def enroll_teacher(self, teacher):
        self.enrolled_teachers.append(teacher)
    
    #  func to print out the details of all enrolled teachers
    def all_teachers(self):
        for each_teacher in self.enrolled_teachers:
            print("Name :" + each_teacher.name)
            print("Lab number :" + each_teacher.lab_number)
            # print("Sports :" + each_teacher.sports)

    # TODO Task2.3: implement a func to get all teachers' data
    def fetch_all_teacher_data(self):
        return self.enrolled_teachers
        # print(self.enrolled_teachers)

    # TODO Task2.4: implement a function get teacher with name
    def fetch_data_with_teacher_name(self):
        for each_teacher in self.enrolled_teachers:
            return each_teacher.name
            # print(each_teacher.name)