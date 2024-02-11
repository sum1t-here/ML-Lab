# A decorator is a design pattern in object-oriented programming 
# that allows behavior to be added to individual objects dynamically, 
# without affecting the behavior of other objects from the same class. 
# It's a structural pattern that allows functionality to be added to 
# objects at runtime through composition.


# In simpler terms, decorators are like adding toppings to a pizza. 
# You start with a base pizza (the original object), and then you can 
# add toppings (decorators) like cheese, pepperoni, or mushrooms to 
# enhance its flavor without changing the base pizza itself. 
# Each topping adds a new layer of flavor, and you can mix and match 
# toppings as desired.

def decorat(func):
    def wrapper():
        print("before greeting")
        func()
        print("after greeting")
    return wrapper

@decorat
def greet():
    print("Hello, How are you?")

@decorat
def welcome():
    print("Welcome, Everyone")


greet()
# before greeting
# Hello, How are you?
# after greeting
welcome()
# before greeting
# Welcome, Everyone
# after greeting

import time

def timing(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"execution time : {end_time - start_time}")
        return result
    return wrapper

@timing
def slow_func():
    print("This is a slow function")
    time.sleep(2)

slow_func()
# This is a slow function
# execution time : 2.0050570964813232