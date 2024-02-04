def add(x, y):
    print(x+y)
#  cannot save the value
i = add(3,4)
print(i) # None

# Non-void function
def Add(x,y):
    return(x+y)

j = Add(3,4)
print(j) # 7

#provide multiple values
def sum(*args):
    val = 0
    for i in args:
        val = val + i
    return(val)

print(sum(2,3,4,5,5,6,6,6,7)) # 44

# multiple value in form of key-value pair
def greetings_location(**kwargs):
    for i,j in kwargs.items():
        print(f"hello {i}, hows the weather at {j}")

greetings_location(CtAmerica = 23, spiderman = 34, Ironman = 12)

# hello CtAmerica, hows the weather at 23
# hello spiderman, hows the weather at 34
# hello Ironman, hows the weather at 12