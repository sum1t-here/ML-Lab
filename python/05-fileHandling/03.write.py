# writing a text file

def greeting(name):
    return f"Hello, how are you {name} ?"

data = greeting("Wanda")

with open("data.txt", "w") as file:
    file.write(data)

with open("data.txt", "r") as file:
    print(file.read())

# Hello, how are you Wanda ?
    
# writing multiple lines of text
    
data = ["line1 \n", "line2 \n", "line3 \n"]

with open("text_lines.txt", "w") as file:
    file.writelines(data)

with open("text_lines.txt", "r") as file:
    for line in file.readlines():
        print(line)

# line1 

# line2 

# line3 
        
# appending data in file
        
new_data = "\n this is additional line data"

with open('text_lines.txt', 'a') as file:
    file.write(new_data)

with open("text_lines.txt", "r") as file:
    for line in file.readlines():
        print(line)

# line1 

# line2 

# line3 



#  this is additional line data