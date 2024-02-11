# __init__

# special method that initialises itself at the start of the class
# it calls itself and allocates space and memory for an object
# set values to be used in the object

# self

# parameter provided by init 
# used to access object variables

class Dog:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

mydog = Dog("tomy",3)
print(f"dog name is {mydog.name}")
# dog name is tomy