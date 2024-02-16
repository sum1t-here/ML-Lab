# Buffering in file handling is a technique where data is stored in a temporary buffer before being read from or written

with open("buffer.txt", 'w', buffering = 2048) as file:
    file.write("this is some random data")
    file.flush() # flush it into the physical memory

data = ["line1 \n", "line2 \2"]

with open("lines.txt", 'w', buffering=1) as file:
    file.writelines(data)

with open("buffer.txt", 'r', buffering=1024) as file:
    print(file.read())
# this is some random data