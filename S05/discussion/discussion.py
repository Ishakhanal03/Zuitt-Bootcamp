# Declaration of a "class" is done using the "Class" statement followed by the ClassName

class SampleClass():
    # the class constructor or initialization method is called by Python everytime an instance of the class is created
    # "self" parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class
    def __init__(self, year):
        # "year" is a property of the class
        self.year = year

    # methods are functions inside a class
    def show_year(self):
        print(f'The year is: {self.year}')

# Creating an object instance of the SampleClass is done by calling the class and supplying the arguments needed
myObj = SampleClass(2020) # 2020 will be passed as the value of the "year" property

# To display the properties and methods of an object instance, the "dot notation" is used
print(myObj.year)
myObj.show_year()


# [SECTION] Fundamentals of OOP
# There are four main fundamental principles in OOP
# Encapsulation
# Inheritance
# Polymorphis
# Abstraction


# [SECTION] Encapsulation
# Encapsulation is a mechanism of wrapping the attributes and code acting on the methods together as a single unit

# In encapsulation, the attributes of a class will be hidden from other classes, and can be accesed only through the methods of their current class.

# Therefore, it is also known as data hiding.

# To achieve encapsulation −
# * Declare the attributes of a class.
# * Provide getter and setter methods to modify and view the attributes values.

# Why encapsulation?
# The fields of a class can be made read-only or write-only.
# A class can have total control over what is stored in its fields.

# The prefix underscore is used as a warning for developers that means:
# "Please be careful about this attribute or method, don’t use it outside of the declared Class"

class Person():
    def __init__(self):
        # protected attribute _name
        self._name = "John Doe"
        # protected attribute _age
        self._age = 0

    # setter method "set_name"
    def set_name(self, name):
        self._name = name

    # getter method "get_name"
    def get_name(self):
        print(f'Name of Person: {self._name}')

    # setter method "set_age"
    def set_age(self, age):
        self._age = age

    # getter method "get_name"
    def get_age(self):
        print(f'Age of Person: {self._age}')

p1 = Person();
# print(p1.name) #this will return an attribute error
print(p1._name)
p1.get_name()
p1.set_name("Bob Doe")
p1.get_name()
p1.get_age()
p1.set_age(38)
p1.get_age()


# [Section] Inheritance
# The transfer of the characteristics of a parent class to child classes that are derived from it.
# An example of this is an employee and a person. An employee is a person with additional attributes and methods
# To create an inherited class, in the ClassName definition, add the parent class
# Syntax: class ChildClassName(ParentClassName)

class Employee(Person):
    def __init__(self, employeeId):
        # super() can be used to invoke immediate parent class constructor
        super().__init__()
        # attribute unique to the Employee class
        self._employeeId = employeeId

    # getter method
    def get_employeeId(self):
        print(f'The Employee ID is {self._employeeId}')

    # setter method
    def set_employeeId(self, employeeId):
        self._employeeId = employeeId

    # details method
    def get_details(self):
        print(f"{self._employeeId} belongs to {self._name}")

emp1 = Employee("Emp-001")
emp1.get_details()
emp1.set_name("Bob Doe")
emp1.set_age(38)
emp1.get_details()

class Student(Person):
    def __init__(self, studentNo, course, year_level):
        # super() can be used to invoke immediate parent class constructor
        super().__init__()
        # attributes unique to the Employee class
        self._studentNo = studentNo
        self._course = course
        self._year_level = year_level
    
    # getters
    def get_studentNo(self):
        print(f"Student number of Student is {self._studentNo}")

    def get_course(self):
        print(f"Course of Student is {self._course}")

    def get_year_level(self):
        print(f"The Year Level of Student is {self._year_level}")

    # setters
    def set_studentNo(self, studentNo):
        self._studentNo = studentNo
    
    def set_course(self, course):
        self._course = course
    
    def set_year_level(self, year_level):
        self._year_level = year_level

    # custom method
    def get_details(self):
        print(f"{self._name} is currently in year {self._year_level} taking up {self._course}.")

# Test cases:
student1 = Student("stdt-001", "Computer Science", 1)
student1.set_name("Brandon Smith")
student1.set_age(18)
student1.get_details()


# [Section] Polymorphism
# A child class inherits all the methods from the parent class. However, in some situations, the method inherited from the parent class doesn’t quite fit into the child class. In such cases, you will have to re-implement method in the child class.

# There are different methods to use polymorphism in Python. You can use different function, class methods or objects to define polymorphism. So, let’s move ahead and have a look at each of these methods in detail.

# Functions and objects
# A function can be created that can take any object, allowing for polymorphism.
class Admin():
    def is_admin(self):
        print(True)

    def user_type(self):
        print('Admin User')

class Customer():
    def is_admin(self):
        print(False)

    def user_type(self):
        print('Regular User')

# Define a test function that will take an object called obj
def test_function(obj):
    obj.is_admin()
    obj.user_type()

# Create object instances for Admin and Customer
user_admin = Admin()
user_customer = Customer()

# Pass the created instances to the test_function
test_function(user_admin)
test_function(user_customer)
# What happens is that the test_function would call the methods of the object passed to it hence allowing it to have different outputs that depend on the object passed.

# Polymorphism with Inheritance

# Polymorphism in Python defines method in the child class tha have the same name as the methods in parent class.
# In inheritance, the child class inherits the methods from the parent class. Also, it is possible to modift a method in a chidl class that it has inherited from the parent class.
# Parent Class
class Zuitt():
    def tracks(self):
        print('We are current offering 3 tracks(developer career, pi-shape carrer, and short courses)')

    def num_of_hours(self):
        print('Learn web development in 360 hours!')

# Child class of Zuitt class
class DeveloperCarrer(Zuitt):
    def num_of_hours(self):
        print('Learn basics of web development in 240 hours!')

class PiShapedCarreer(Zuitt):
    def num_of_hours(self):
        print('Learn skills for no-code app development in 140 hours!')

class ShortCourses(Zuitt):
    def num_of_hours(self):
        print('learn advanced topics in web development in 20 hours!')

zuitt = Zuitt()
course1 = DeveloperCarrer()
course2 = PiShapedCarreer()
course3 = ShortCourses()

zuitt.num_of_hours()
course1.num_of_hours()
course2.num_of_hours()
course3.num_of_hours()

# Abstraction
# An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class.

# By default, Python does not provide abstact classes. Python comes with a module that will let us create abstract classes.

# import the ABC model and the annotcation abcstractclassmethod
from abc import ABC, abstractclassmethod

# Abstract class

class Polygon(ABC):

    # Create an abstract method
    @abstractclassmethod
    def printNumberOfSides(self):
        # pass keyword denotes that the method will do nothing.
        pass


# Child class of the Abstract Class

class Triangle(Polygon):
    def __init__(self):
        super().__init__()

    def printNumberOfSides(self):
        print(f"This polygon has 3 sides.")

class Pentagon(Polygon):
    def __init__(self):
        super().__init__()

    def printNumberOfSides(self):
        print(f"This polygon has 5 sides.")


shape1 = Triangle()
shape1.printNumberOfSides();

shape2 = Pentagon()
shape2.printNumberOfSides();