temp_c = [10, 20, 30, 40]
temp_f = list(map(lambda x: (9/5)*x + 32, temp_c))
print(temp_f)
# [50.0, 68.0, 86.0, 104.0]


names = ['Ironman', 'Hulk', 'Spiderman']
age = [30, 32, 20]
comb_val = list(map(lambda name,age: f"age of {name} is {age} years old", names, age))
print(comb_val)
# ['age of Ironman is 30 years old', 'age of Hulk is 32 years old', 'age of Spiderman is 20 years old']

num = [[1,2,3], [4,5,6], [7,8,9]]
sq_matrix = list(map(lambda row: list(map(lambda x : x**2,row)),num))
print(sq_matrix)
# [[1, 4, 9], [16, 25, 36], [49, 64, 81]]