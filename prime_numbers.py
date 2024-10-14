def prime_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield num

# Example: Find primes between 10 and 50
start = 10
end = 50
prime_numbers = prime_range(start, end)
print(next(prime_numbers))
print(next(prime_numbers))
print(next(prime_numbers))
print(next(prime_numbers))
print(next(prime_numbers))
print(next(prime_numbers))