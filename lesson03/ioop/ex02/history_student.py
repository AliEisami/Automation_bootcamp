from student import Student

class HistoryStudent(Student):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._grade_a = 100
        self._grade_b = 100
        self._grade_c = 100

    @property
    def grade_a(self):
        return self._grade_a

    @property
    def grade_b(self):
        return self._grade_b

    @property
    def grade_c(self):
        return self._grade_c

    @grade_a.setter
    def grade_a(self, grade_a):
        self._grade_a = grade_a

    @grade_b.setter
    def grade_b(self, grade_b):
        self._grade_b = grade_b

    @grade_c.setter
    def grade_c(self, grade_c):
        self._grade_c = grade_c