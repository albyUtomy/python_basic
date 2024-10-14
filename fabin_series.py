def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Testing the generator
fib_gen = fibonacci_generator(10)

for i in range(0,10):
    print(next(fib_gen), ends=" ")

