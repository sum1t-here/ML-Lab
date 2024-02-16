with open('testing.txt','w') as file:
    file.write("Sample testing")
    file.close

with open('testing.txt','r') as file:
    content=file.read()
    print(content) # Sample testing
    file.close

with open('testing.txt','r') as file:
    content=file.read(10)
    position=file.tell()
    print(f"data = {content}, position = {position}") # data = Sample tes, position = 10

with open('testing.txt','r') as file:
    file.seek(3)
    content=file.read(10)
    print(content) # ple testin

file = open('testing.txt', 'r+')
file.truncate(5)
content = file.read()
print(content) # Sampl

file = open('testing.txt',"r")
print("is file readable",file.readable())
print("is file writable",file.writable())
print("is file seekable",file.seekable())
desc = file.fileno()
print(desc) # 4
print("is file closable",file.closed)
file.close()
print("is file closable",file.closed)


# is file readable True
# is file writable False
# is file seekable True
# is file closable False
# is file closable True

with open("testing2.txt","w") as file:
    file.write("testing 2 data")

with open("testing.txt", 'r') as source, open("testing3.txt","w") as destination:
    destination.write(source.read())

import os
os.remove('testing.txt')

os.path.exists('testing.txt')
print(os.stat('testing2.txt'))
os.rename('testing2.txt','hi.txt')

os.makedirs('content')
with open(os.path.join('content','testing2.txt'), 'w') as file:
    file.write('data is in new directory file')