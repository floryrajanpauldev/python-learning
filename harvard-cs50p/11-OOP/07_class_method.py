#Class method – @classmethod
import random

class Student:
    students = ["John", "Mary", "David", "Sarah"]

    @classmethod
    def pick_student(cls):
        return random.choice(cls.students)

print(Student.pick_student())