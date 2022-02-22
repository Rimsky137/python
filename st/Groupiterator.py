class GroupIterator:
    def __init__(self, student_list):
        self.list_students = student_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.student_list):
            raise StopIteration()
        temp_student = self.student_list[self.index]
        self.index += 1
        return temp_student
