from models.student import Student

class TestStudent:
    def test_calculate_year_of_birth(self):
        st = Student(name="Test name", age=29, class_number=2)
        assert st.calculate_year_of_birth(2022) == 1992
