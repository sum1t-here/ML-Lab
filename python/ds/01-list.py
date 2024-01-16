# A list is one of the most versatile and commonly used data structures in Python
# It is an ordered collection of elements that can be of any data type, such as integers, strings, or other lists
# Lists are mutable, which means you can change their contents after creation
# You can access elements by their index, and you can perform various operations like adding,removing, or sorting elements

# creating a list of numbers

numbers = [1,2,3,4]
# accessing and printing the third element
print("The third number is:",numbers[2])
# The third number is: 3

# creating a list of phones

Phones = ["Realme", "Mi", "Samsung", "Iphone"]
# Adding new phones to the list
Phones.append("Oppo")
# Removing phones from the list
Phones.remove("Mi")
# Printing updated list
print("Updated list of phones:",Phones)
# Updated list of phones: ['Realme', 'Samsung', 'Iphone', 'Oppo']

# creating list with mixed data types

info = ["Julie", 21, 1.75, True]
# Accessing and printing the elements
name = info[0]
age = info[1]

print(f"Name is {name} and age is {age}")
# Name is Julie and age is 21

# creating a list of lists

matrix = [[1,2,3], [4,5,6], [7,8,9]]
# Accessing and printing a specific element
element = matrix[1][2]
print(f"Element at row 1 and column 2: {element}")
# Element at row 1 and column 2: 6

# Real world analogy

# creating a shopping list
shopping_list = ["Apples", "Orange", "Banana", "Milk"]
item = "Milk"

if item in shopping_list:
    print(f"{item} is in Shopping List")
else:
    print(f"{item} is not in Shopping List")
# Milk is in Shopping List