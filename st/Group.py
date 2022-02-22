class Group:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        if len(self.student_list) < 10:
            self.student_list.append(student)
        else:
            try:
                raise TooManyStudentsException("Too many students!")
            except TooManyStudentsException as err:
                print(err.get_exception_message())

    def remove_student(self, student):
        self.student_list.remove(student)

    def search(self, name):
        for student in self.student_list:
            if student.name == name:
                return student.__str__()

    def __str__(self):
        str = ""
        for student in self.student_list:
            str += student.__str__()
        return str      
