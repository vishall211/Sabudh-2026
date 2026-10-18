from abc import ABC, abstractmethod

# --------------------------------------
# TASK 1: ABSTRACTION - PERSON CLASS
# --------------------------------------
class Person(ABC):

    def __init__(self, Name, age, gender, address):
        self.Name = Name
        self.age = age
        self.gender = gender
        self.address = address

    # Display person details
    def __str__(self):
        return f"Name : {self.Name}, Age : {self.age}, Gender : {self.gender}, Address : {self.address}"

    # Greet another person
    def greet(self, other_person):
        print(f"Hello {other_person.Name}! This is {self.Name}.")

    # Child classes must implement this method
    @abstractmethod
    def introduce(self):
        pass

    # Check whether the person is an adult
    @staticmethod
    def is_adult(age):
        return age >= 18


# --------------------------------------
# TASK 2: SINGLE INHERITANCE - EMPLOYEE
# --------------------------------------

class Employee(Person):

    counter = 0

    def __init__(self, Name, age, gender, address, salary):
        super().__init__(Name, age, gender, address)

        self._salary = salary

        # Generate employee ID
        Employee.counter += 1
        self.__employee_id = f"EMP{Employee.counter:02d}"

    # Decrease counter when employee is deleted
    def __del__(self):
        if Employee.counter > 0:
            Employee.counter -= 1

    # Return total number of employees
    @property
    def employee_count(self):
        return Employee.counter

    # Getter for employee ID
    @property
    def employee_id(self):
        return self.__employee_id

    # Getter for salary
    @property
    def salary(self):
        return self._salary

    # Setter for salary
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

    # Increase salary
    def increase_salary(self, amount):
        self._salary += amount

    # Decrease salary
    def decrease_salary(self, amount):
        self._salary -= amount

    # Implement abstract method
    def introduce(self):
        return f"Hello, my name is {self.Name} and I work as an employee."


# --------------------------------------
# TASK 3: POLYMORPHISM - TEACHER CLASS
# --------------------------------------

class Teacher(Employee):

    counter = 0

    def __init__(self, Name, age, gender, address, salary, subjects):

        # Call parent constructor
        super().__init__(Name, age, gender, address, salary)

        self.subjects = subjects

        # Generate teacher ID
        Teacher.counter += 1
        self.__teacher_id = f"TEC{Teacher.counter:02d}"

    # Decrease counter when teacher is deleted
    def __del__(self):
        super().__del__()

        if Teacher.counter > 0:
            Teacher.counter -= 1

    # Return total number of teachers
    @property
    def teacher_count(self):
        return Teacher.counter

    # Getter for teacher ID
    @property
    def teacher_id(self):
        return self.__teacher_id

    # Add one or more subjects
    def add_subject(self, subject):
        new_subjects = subject.split(",")

        for item in new_subjects:
            item = item.strip()

            if item and item not in self.subjects:
                self.subjects.append(item)

    # Remove a subject
    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

    # Override introduce method
    def introduce(self):
        return f"My ID is {self.__teacher_id} and I teach: {', '.join(self.subjects)}"

    # Restrict access to employee ID
    @property
    def employee_id(self):
        raise AttributeError(
            f"{self.__class__.__name__} object has no attribute 'employee_id'"
        )


# --------------------------------------
# MAIN EXECUTION
# --------------------------------------

if __name__ == "__main__":

    # Take teacher details from the user
    name = input("\nEnter teacher name : ")
    age = int(input("Enter teacher age : "))
    gender = input("Enter teacher gender : ")
    address = input("Enter teacher address : ")
    salary = float(input("Enter teacher salary : "))

    # Take subjects as comma-separated input
    subjects = input("Enter subjects (separated by commas) : ").split(",")

    # Remove extra spaces from subject names
    subjects = [subject.strip() for subject in subjects]

    # Create teacher object
    teacher1 = Teacher(name, age, gender, address, salary, subjects)

    # Display teacher details
    print("\n---------- Teacher Details ----------")

    print(teacher1)

    print("Teacher ID :", teacher1.teacher_id)
    print("Salary :", teacher1.salary)
    print("Subjects :", teacher1.subjects)
    print("Teacher Count :", teacher1.teacher_count)

    # Add a subject
    new_subject = input("\nEnter subject to add : ")
    teacher1.add_subject(new_subject)

    print("After Adding Subject :", teacher1.subjects)

    # Remove a subject
    remove_subject = input("\nEnter subject to remove : ")
    teacher1.remove_subject(remove_subject)

    print("After Removing Subject :", teacher1.subjects)

    # Display teacher introduction
    print("\nIntroduction :")
    print(teacher1.introduce())

    # Check employee ID restriction
    print("\nChecking Employee ID :")

    try:
        print(teacher1.employee_id)

    except AttributeError as error:
        print(error)

print("\n")