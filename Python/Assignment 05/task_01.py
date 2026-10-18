from abc import ABC, abstractmethod

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
        print(f"Hello {other_person.Name}! My name is {self.Name}.")

    # Child classes must implement this method
    @abstractmethod
    def introduce(self):
        pass

    # Check whether the person is an adult
    @staticmethod
    def is_adult(age):
        return age >= 18


# Take input from the user
name = input("\nEnter your name : ")
age = int(input("Enter your age : "))
gender = input("Enter your gender : ")
address = input("Enter your address : ")


# Create a simple child class to test Person
class Student(Person):

    def introduce(self):
        return f"Hello, this is {self.Name}."


# Create object using user input
person1 = Student(name, age, gender, address)


# Display results
print("\nPerson Details")
print(person1)

print("\nIntroduction :")
print(person1.introduce())

print("\nIs Adult ?")
print(Person.is_adult(person1.age),"\n")