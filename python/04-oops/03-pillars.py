# encapsulation

# Encapsulation is one of the fundamental principles of object-oriented programming (OOP) that involves bundling data (attributes) 
# and methods (functions) that operate on the data into a single unit, called a class. Encapsulation helps in hiding the internal 
# state of an object from the outside world and only exposing the necessary functionalities to interact with that object.

class Person:
    def __init__(self,name,age):
        self.__name = name # __ set the variable as pvt
        self.__age = age

    def get_name(self):
        return self.__name

    def set_age(self,new_age):
        self.__age = new_age
        return self.__age

person = Person("SteveRogers",25)
print(f"name of person is {person.get_name()}")
# name of person is SteveRogers

# inheritance

# Inheritance is a fundamental concept in object-oriented programming (OOP) 
# that allows a new class (derived class or subclass) to inherit properties 
# and behaviors (attributes and methods) from an existing class (base class, 
# parent class, or superclass). The subclass can then extend or modify the 
# inherited properties and behaviors and also introduce its own unique 
# properties and behaviors.

class Car:
    def __init__(self,engine,tyre):
        self.engine = engine
        self.tyre = tyre

class Maruti(Car):
    def price(self):
        print(f"Price of car for engine {self.engine} is 10000")

maruti = Maruti(1000, 4)
maruti.price()
# Price of car for engine 1000 is 10000

# Polymorphism

# Polymorphism is a core concept in object-oriented programming (OOP) 
# that allows objects of different classes to be treated as objects 
# of a common superclass. It enables a single interface to represent 
# different underlying forms (types) and behaviors. Polymorphism allows 
# methods to behave differently based on the object they are called on,
# promoting flexibility and code reuse.

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius
    

class rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    
# Abstraction
    
# Abstraction is simplifying complex reality by modeling classes appropriate to the problem 
# and working at the most relevant level of detail. It is one of the key principles of 
# object-oriented programming (OOP) and software engineering.
    
from abc import ABC, abstractmethod

class Car:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Sedan(Car):
    def start(self):
        print("car is starting")
    def stop(self):
        print("car is stoping")