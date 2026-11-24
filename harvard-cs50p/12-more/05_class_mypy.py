class Student:
    SCHOOL_NAME: str = "ABC School"

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def display(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {Student.SCHOOL_NAME}")


student = Student("Flory", 25)
student.display()