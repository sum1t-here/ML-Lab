## Explicit type casting

#convert a float to an integer

float_num = 10.7
int_num = int(float_num)
print(int_num) # 10
print(type(int_num)) # <class 'int'>

#convert a string to an integer

# str_num = "five" # this will give an error as five can't be represented as int
str_num = 5 # this will work fine

# convert a data type to boolean

int_num = 0 
str_num = ""

bool_int = bool(int_num)
bool_str = bool(str_num)

print(bool_int) # False
print(bool_str) # False

# Everyhting except 0 in case of int and empty string in case of str is false


# Implicit type casting

a = 5
b = 4.5
print(type(a))
print(type(b))
# <class 'int'>
# <class 'float'>
c = a + b
print(c)
print(type(c))
# 9.5
# <class 'float'>

d = "hello" + 3 # implicit type casting will not happen here         