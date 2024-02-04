add = lambda x, y: x+y
print(add(5,6))  # 11

comp = lambda x,y: x if x > y else y
print(comp(5,6))

fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
# least variable comprehension
seq = [fib(i) for i in range(10)]
print(seq)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]