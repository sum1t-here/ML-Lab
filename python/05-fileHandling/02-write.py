with open("test.txt","r") as file:
    content = file.read()
    print(content)

# Testing a text file
    
# generating files
    
import csv
data = [
    ["name", "age", "city"],
    ["Roger", 28, "Manhettan"],
    ["Stark", 29, "New York"]
]

with open('csv_file.csv', "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)