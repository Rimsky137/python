import Human

class Student(Human):
    def __init__(self, name, surname, age, gender, group_num):
        super().__init__(name, surname, age, gender)
        self.group_num = group_num

    def __str__(self):
        return super().__str__() + " group_num={}".format(self.group_num)
