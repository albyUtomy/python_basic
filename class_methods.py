# Define a simple class
class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed  # Instance attribute

    # Method to make the dog speak
    def bark(self):
        return f"{self.name} says Woof!"

    def __str__(self):
        return self.name
    
# Create an object (instance) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Access attributes and methods
print(my_dog.name)      # Output: Buddy
print(my_dog.breed)     # Output: Golden Retriever
print(my_dog.bark())    # Output: Buddy says Woof!

my_dog_2 = Dog("Ricky", "Street Dog")
print()
print(my_dog_2.name)      # Output: Buddy
print(my_dog_2.breed)     # Output: Golden Retriever
print(my_dog_2.bark())    # Output: Buddy says Woof!
print(my_dog_2)

a = "bark"

print(getattr(my_dog,a))