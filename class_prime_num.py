class Prime:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop 

    def isPrimeRange(self):
        """Yield prime numbers in the range from start to stop."""
        for num in range(self.start, self.stop + 1):
            if num > 1:
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    yield num

    def isPrime(self, i):
        """Check if a number is prime."""
        if i <= 1:
            return False
        for n in range(2, int(i ** 0.5) + 1):
            if i % n == 0:
                return False
        return True


# User input to select the option
while True:
    option = int(input("Enter an option from the given below: \n[1] Prime of range\n[2] A number is prime or not\n[3] Exit\n"))

    if option == 1:
        start = int(input("Enter the starting number: "))
        stop = int(input("Enter the ending number: "))
        prime_obj = Prime(start, stop)
        print("Prime numbers in range:")
        print(list(prime_obj.isPrimeRange()))  # Convert the generator to a list to print all primes

    elif option == 2:
        number = int(input("Enter a number to check if it's prime: "))
        prime_obj = Prime(0, 0)  # Create an object but these values won't be used
        if prime_obj.isPrime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    
    elif option == 3:
        print("Exiting the program.")
        break  # Exit the loop and terminate the program

    else:
        print("Invalid option selected. Please try again.")
