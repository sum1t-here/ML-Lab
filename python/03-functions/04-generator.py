def generator():
    yield 10
    yield 20
    yield 30

gen = generator()
print(next(gen)) # 10
print(next(gen)) # 20
print(next(gen)) # 30
# print(next(gen)) # Err



# fib = 0, 1, 2, 3, 5, 8
def fibonacci_gen():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

fib = fibonacci_gen()
for _ in range(10):
    print(next(fib))


# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34