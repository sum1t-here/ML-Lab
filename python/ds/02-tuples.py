# Tuples are similar to lists,but they are immutable.
# Once you create a tuple, you cannot change its content.This immutability makes tuples
# useful for situations where you want to ensure that the data remains constant.
# They are often used to represent collections of related values.

# tuple to store co-ordinate

point = (3,4)
print("X coordinate is", point[0])
print("Y coordinate is", point[1])
# X coordinate is 3
# Y coordinate is 4

# Packing values into a tuple
person = ("Arjun", 28, "Banglore")
# unpacking
name, age, city =  person
print(f"Name: {name}, Age: {age}, City: {city}")
# Name: Arjun, Age: 28, City: Banglore

# Simulating a function that returns multiple values
def get_student_info():
    name = "Arun"
    age = 21
    grade = "A"
    return name, age, grade

student_info = get_student_info()
name, age, grade = student_info
print(f"Name: {name}, Age: {age}, Grade: {grade}")
# Name: Arun, Age: 21, Grade: A

# combining two tuples
colors1 = ("red","green","yellow")
colors2 = ("yellow","orange")

combined_colors = colors1+colors2
print("Combined colors: ",{combined_colors})
# Combined colors:  {('red', 'green', 'yellow', 'yellow', 'orange')}

# Define tuples to represent boxes of chocolates
box1 = ("Dark Chocolate", "Milk Chocolate", "White Chocolate")
box2 = ("Caramel Chocolate", "Hazelnut Chocolate")
box3 = ("Raspberry Chocolate", "Coconut Chocolate")
# Combine the boxes into a larger bag
chocolate_bag = (box1, box2, box3)
# Access the chocolates in the bag
for box in chocolate_bag:
  print("Box contents:")
  for chocolate in box:
      print(" - " + chocolate)
# Box contents:
#  - Dark Chocolate
#  - Milk Chocolate
#  - White Chocolate
# Box contents:
#  - Caramel Chocolate
#  - Hazelnut Chocolate
# Box contents:
#  - Raspberry Chocolate
#  - Coconut Chocolate