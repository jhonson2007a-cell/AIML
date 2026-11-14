#data-24oct, 2026
#method in python
#decroreter in interview

# class demo:
#     def hello(self):
#         print("hello")
# d=demo()
# d.hello()

#decoretor
'''class demo():
    @staticmethod
    def welcome():
        print("welcome")
demo.welcome()'''

# class Student:
#     def __init__(self, marks):
#         self.__marks = marks
#     # Getter property
#     @property
#     def marks(self):
#         return self.__marks
#     # Setter property
#     @marks.setter
#     def marks(self, value):
#         if 0 <= value <= 100:
#             self.__marks = value
#         else:
#             print("Marks must be between 0 and 100")
# s1 = Student(80)
# print(s1.marks)
# s1.marks = 95
# print(s1.marks)
# s1.marks = 150

# class Person:
#     def __init__(self, name):
#         self.__name = name
#     @property
#     def name(self):
#         return self.__name
# p = Person("Amit")
# print(p.name)


# class Product:
#     def __init__(self, price):
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price
# p = Product(500)
# print(p.price)

# class Student:
#     def __init__(self, marks):
#         self.__marks = marks
#     @property
#     def marks(self):
#         return self.__marks
#     @marks.setter
#     def marks(self, value):
#         if 0 <= value <= 100:
#             self.__marks = value
#         else:
#             print("Invalid marks")
# s = Student(70)
# s.marks = 85
# print(s.marks)

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary
#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self, value):
#         if value >= 0:
#             self.__salary = value
#         else:
#             print("Invalid salary")
            
# e = Employee(30000)
# e.salary = 35000
# print(e.salary)

# Create a Rectangle class with length and width properties. Reject non-positive values and calculate area.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     @property
#     def length(self):
#         return self.__length
#     @length.setter
#     def length(self, value):
#         if value > 0:
#             self.__length = value
#         else:
#             raise ValueError("Length must be positive")
#     @property
#     def width(self):
#         return self.__width
#     @width.setter
#     def width(self, value):
#         if value > 0:
#             self.__width = value
#         else:
#             raise ValueError("Width must be positive")
#     @property
#     def area(self):
#         return self.length * self.width
# r = Rectangle(5, 4)
# print(r.area)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     # Method to display student details
#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)

# # Create a student object
# s1 = Student("Harsh", 85)
# # Display student information
# s1.display()

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def display(self):
#         print(self.name, self.balance)
# account = BankAccount("Amit", 5000)
# account.display()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)

# e1 = Employee("Rahul", 30000)
# e1.display()

# class Student:
#     def __init__(self, marks):
#         self.marks = marks
#         print("Old Marks:",self.marks)
#     def update_marks(self, new_marks):
#         self.marks = new_marks
#     def display(self):
#         print("Updated_Marks:", self.marks)

# s1 = Student(70)
# s1.update_marks(85)
# s1.display()


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(self.price)
#     def apply_discount(self):
#         self.price = self.price * 0.90
# p1 = Product("Book", 500)
# p1.apply_discount()
# print("Price:",p1.price)

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#         print("Account created successfully!")
#         print("Initial Balance:", self.balance)
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print("Deposited Amount:", amount)
#             print("Deposit successful!")
#         else:
#             print("Invalid deposit amount")
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid withdrawal amount")
#         elif amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print("Withdrawn Amount:", amount)
#             print("Withdrawal successful!")
#     def display(self):
#         print("Current Balance:", self.balance)
# account = BankAccount(1000)
# print("\n--- Deposit ---")
# account.deposit(500)
# print("\n--- Withdrawal ---")
# account.withdraw(300)
# print("\n--- Account Details ---")
# account.display()

#Inheritance
# Parent class
'''class Person:
    def show_name(self):
        print("I am a person")
# Child class
class Student(Person):
    pass
# Create a child object
s1 = Student()
# Use the inherited method
s1.show_name()'''


'''class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    pass
d = Dog()
d.eat()'''

'''class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    pass
c = Car()
c.start()'''

'''class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    pass
s = Student("Harsh")
print(s.name)'''

'''class Device:
    def info(self):
        print("Electronic device")
class Laptop(Device):
    def work(self):
        print("Laptop is working")
l = Laptop()
l.info()
l.work()'''

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
    def display(self):
        print(self.name, self.age, self.roll_number)
s = Student("Harsh", 22, 101)
s.display()'''

'''class Person:
    def person_info(self):
        print("Person class")
class Student(Person):
    def student_info(self):
        print("Student class")
s = Student()
s.person_info()
s.student_info()'''

'''class Animal:
    def eat(self):
        print("Eating")
class Cat(Animal):
    pass
Cat().eat()'''

'''class A:
    def show_a(self):
        print("A")
class B(A):
    pass
class C(B):
    pass
C().show_a()'''

'''# Medium: Multiple inheritance
# Create a class that inherits from both Father and Mother.
class Father:
    def skill1(self):
        print("Gardening")
class Mother:
    def skill2(self):
        print("Cooking")
class Child(Father, Mother):
    pass
c = Child()
c.skill1()
c.skill2()'''

'''# Medium: Hierarchical inheritance
# # Create Animal as a parent class with two child classes Dog and Cat.
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
Dog().eat()
Cat().eat()'''


'''# Hard: Hybrid inheritance
# Create a small hybrid inheritance structure using Person, Student, Employee, and TeachingAssistant, where the last class inherits from both Student and Employee.
class Person:
    def identity(self):
        print("Person")
class Student(Person):
    def study(self):
        print("Studying")
class Employee(Person):
    def work(self):
        print("Working")
class TeachingAssistant(Student, Employee):
    pass
ta = TeachingAssistant()
ta.identity()
ta.study()
ta.work()'''

#overriding
'''class Person:
    def role(self):
        print("I am a person")
class Student(Person):
    # Overriding the parent method
    def role(self):
        print("I am a student")
p = Person()
s = Student()
p.role()
s.role()'''


'''class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Bark")

Dog().sound()'''


'''# Override a display() method in a child class.
class A:
    def display(self):
        print("A")
class B(A):
    def display(self):
        print("B")
B().display()'''


'''# Create Employee and Manager classes. Override the role() method in Manager.
class Employee:
    def role(self):
        print("Employee")
class Manager(Employee):
    def role(self):
        print("Manager")
Manager().role()'''

'''# Override a parent method that returns a number and display the child result.
class Calculator:
    def value(self):
        return 10
class AdvancedCalculator(Calculator):
    def value(self):
        return 20
print(AdvancedCalculator().value())'''


'''# Create a Student parent class and a GraduateStudent child class. 
# Both should have a display_type() method with different messages.
class Student:
    def display_type(self):
        print("Regular Student")
class GraduateStudent(Student):
    def display_type(self):
        print("Graduate Student")
Student().display_type()
GraduateStudent().display_type()'''