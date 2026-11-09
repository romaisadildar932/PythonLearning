#constructor -> automatically called when an object is created......__init__() is a special method in Python classes that is used to initialize the attributes of an object when it is created. It is called a constructor because it constructs the object and sets its initial state.
'''syntax:
class ClassName:
    def __init__(self, attribute1, attribute2, ...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        
        3 types of contructors:
        1. Default constructor: A constructor that takes no arguments and initializes the object with default values.(self)
        2. Parameterized constructor: A constructor that takes arguments and initializes the object with the provided values.(self,name,age,marks)
        3. constructor with default values: A constructor that takes arguments with default values and initializes the object with the provided or default values.(self,name='John',age=18,marks=0)'''

#default constructor
class Animal:
    def __init__(self): #constructor without attributes
        print("Animal is created")
cat = Animal() 

#parameterized constructor
class Car:
    def __init__(self, model, color): #constructor with attributes
        self.model = model
        self.color = color

    def show_details(self):
        print("Car model:", self.model)
        print("Car color:", self.color)
car1 = Car('Tesla', 'Red') #Creates an object (instance) of the Car class and initializes its attributes using the constructor.
car1.show_details()

#Another example of constructor with attributes
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student('Romaisa',20,'A+')
student2 = Student('Ayesha',21,'B')

print("Student 1 name:", student1.name)
print("Student 1 age:", student1.age)
print("Student 1 grade:", student1.grade)
print(f'Student 2 name: {student2.name}, age: {student2.age}, grade: {student2.grade}')

#constructor with default values
class Employee:
    def __init__(self, name='John', age=18, salary=0):
        self.name = name
        self.age = age
        self.salary = salary
emp1 = Employee()
print(f'Employee 1 name: {emp1.name}, age: {emp1.age}, salary: {emp1.salary}')