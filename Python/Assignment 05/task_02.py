from abc import ABC, abstractmethod

# Parent class
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

    @abstractmethod
    def introduce(self):
        pass

    @staticmethod
    def is_adult(age):
        return age >= 18


# Child class
class Employee(Person):
    
    counter = 0

    def __init__(self, Name, age, gender, address, salary):

        # Call parent constructor
        super().__init__(Name, age, gender, address)

        self._salary = salary

        # Here i am generating employee ID
        Employee.counter += 1
        self.__employee_id = f"EMP{Employee.counter:02d}"

    # Decrease counter when object is deleted
    def __del__(self):
        Employee.counter -= 1

    # Return total employees
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


# Taking input from the user
name = input("\nEnter employee name : ")
age = int(input("Enter employee age : "))
gender = input("Enter employee gender : ")
address = input("Enter employee address : ")
salary = float(input("Enter employee salary : "))


# Creating employee object
employee1 = Employee(name, age, gender, address, salary)


# Display employee details
print("\n---------- Employee Details ----------")
print(employee1)

print("Employee ID :", employee1.employee_id)
print("Salary:", employee1.salary)
print("Employee Count:", employee1.employee_count)

# Increase salary
amount = float(input("\nEnter amount to increase salary : "))
employee1.increase_salary(amount)

print("Updated Salary:", employee1.salary)

# Decrease salary
amount = float(input("\nEnter amount to decrease salary : "))
employee1.decrease_salary(amount)

print("Salary after decrease:", employee1.salary)

# Display introduction
print("\nIntroduction :")
print(employee1.introduce(),"\n")