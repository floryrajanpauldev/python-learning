class Employee:
    COMPANY_NAME = "ABC Technologies"
    MAX_VACATION_DAYS = 20

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {Employee.COMPANY_NAME}")
        print(f"Vacation Days: {Employee.MAX_VACATION_DAYS}")


employee1 = Employee("Smith", 80000)
employee2 = Employee("John", 90000)

employee1.display()
employee2.display()

"""
Name: Smith
Salary: 80000
Company: ABC Technologies
Vacation Days: 20

Name: John
Salary: 90000
Company: ABC Technologies
Vacation Days: 20

"""