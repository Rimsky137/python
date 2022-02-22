import Student 
import Group


student_1 = Student("Roman", "Petrov", "18", "male", 1)
student_2 = Student("Nina", "Ivanova", "19", "female", 2)
student_3 = Student("Ivan", "Smirnov", "20", "male", 3)
student_4 = Student("Olya", "Popova", "21", "female", 4)

group_1 = Group()
group_2 = Group()
group_3 = Group()
group_4 = Group()
group_1.add_student(student_1)
group_2.add_student(student_2)
group_3.add_student(student_3)
group_4.add_student(student_4)

print(group_1)
print(group_2)
print(group_3.search("Ivan"))
