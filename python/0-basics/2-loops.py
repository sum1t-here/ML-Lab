# For loop

# Printing a list of courses

courses = ["Data Science", "Data Analytics", "Javascript", "Python"]

for course in courses:
    print(course)

# Data Science
# Data Analytics
# Javascript
# Python
    
# Generating a number sequence

for i in range(1, 6):
    print('Number :', i)

# for range(5) --> this will iterate from i = 0 to i = n
# range(1,n) --> from 1 to n-1
# range(1,n,2) --> 2 at last means there will be a jump of 2 iteration
    
# Counting and displaying course name
    
count = 0

for course in courses:
    print(f"course {count} : {course}")
    count += 1
print(count)

# course 1 : Data Science
# course 2 : Data Analytics
# course 3 : Javascript
# course 4 : Python
# 4

# Finding the length of each course

for course in courses:
    length = len(course)
    print(f"The course name {course} has {length} characters")

# The course name Data Science has 12 characters
# The course name Data Analytics has 14 characters
# The course name Javascript has 10 characters
# The course name Python has 6 characters
    
# Nested for loop
    
# star
    
for i in range(5):
    for j in range(i+1):
        print("*", end=" ")
    print()

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

for i in range(4):
    for j in range(4):
       print("*", end=" ")
    print()


# * * * * 
# * * * * 
# * * * * 
# * * * * 

# counting down
      
count = 5

while count > 0:
    print(count)
    count -= 1

# 5
# 4
# 3
# 2
# 1
    
# validation
    
# valid_input = False
# while not valid_input:
#      user_input = input("Enter 'yes' or 'no': ")
#      if user_input.lower() in ["yes", "no"]:
#        valid_input = True
#      else:
#       print("Invalid input. Please enter 'yes' or 'no'.")

# Creating a matrix
      
rows = 3
cols = 3
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i*cols+j)
    matrix.append(row)

for row in matrix:
    print(row)

# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]
    
# matrix multiplication
    
matrix_A = [[1,2,3], [4,5,6], [7,8,9]]
matrix_B = [[9,8,7], [6,5,4], [9,8,7]]

result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(matrix_A)):
    for j in range(len(matrix_B[0])):
        for k in range(len(matrix_B)):
            result[i][j] += matrix_A[i][k] * matrix_B[k][j]

for row in result:
    print(row)

# [48, 42, 36]
# [120, 105, 90]
# [192, 168, 144]