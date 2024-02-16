with open('data.txt', 'r') as file:
    print(file.read(10))

# Hello, how
    
with open('data.txt', 'r') as file:
    print(file.read().split())

# ['Hello,', 'how', 'are', 'you', 'Wanda', '?']

import csv 

with open('csv_file.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# ['name', 'age', 'city']
# ['Roger', '28', 'Manhettan']
# ['Stark', '29', 'New York']
