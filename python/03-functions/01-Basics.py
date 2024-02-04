# def greetings():
#     # It will greet people
#     name = input("Hello, may I know your name ?")
#     print(f"Hi {name}, How are you ?")

# greetings()

# Hello, may I know your name ?Sumit
# Hi Sumit, How are you ?

def greeting(name = "User", location="India"):
    # it will greet people
    print(f"Hi {name}, How are you?")
    print(f"What's the weather in {location}")

names = ["Ct.America", "Iron man", "krissh"]
locations = ["New york", "USA", "India"]
for name,location in zip(names,locations):
    greeting(name, location)

# Hi Ct.America, How are you?
# Hi Iron man, How are you?
# Hi krissh, How are you?
    
# Hi Ct.America, How are you?
# What's the weather in New york
# Hi Iron man, How are you?
# What's the weather in USA
# Hi krissh, How are you?
# What's the weather in India
    
greeting()

# Hi User, How are you?
# What's the weather in India