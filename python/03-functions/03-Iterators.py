val = [1,2,3,4,5,56,7]

x = iter(val)

# Evverytime running this provide the next value every time
print(next(x, "End"))
print(next(x, "End"))
print(next(x, "End"))
print(next(x, "End"))
print(next(x, "End"))
print(next(x, "End"))
print(next(x, "End"))
print(next(x, "End"))

# 1
# 2
# 3
# 4
# 5
# 56
# 7
# End