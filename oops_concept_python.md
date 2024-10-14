# Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" and "classes" to structure software. OOP enables modularity, code reusability, and easier maintenance.

## Key OOP Concepts:

1. **Classes and Objects**
2. **Encapsulation**
3. **Abstraction**
4. **Inheritance**
5. **Polymorphism**
6. **Method Overriding**
7. **Method Overloading**
8. **Constructors and Destructors**

---

## 1. Classes and Objects

- **Class**: A blueprint for creating objects (instances). It defines a set of attributes and methods that the created objects will have.
- **Object**: An instance of a class. Each object can have different values for the attributes defined in the class.

### Example:
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}")

# Creating an object
car1 = Car("Toyota", "Corolla")
car1.display_info()  # Output: Car Make: Toyota, Model: Corolla
```
---


## 2. Encapsulation
Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit, i.e., a class. It also restricts access to some attributes to ensure data integrity.

In Python, you can make attributes private by prefixing them with two underscores ```(__)```.
Example:
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance

# Example usage:
account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

```
---

## 3. Abstraction
Abstraction is the concept of hiding complex implementation details and exposing only essential functionalities. In Python, abstraction can be achieved through abstract classes and methods, using the abc module.

Example:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Example usage:
dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
```
---

## 4. Inheritance
Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class), promoting code reuse and scalability.

Example:
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_car_info(self):
        self.display_info()
        print(f"Doors: {self.doors}")

# Example usage:
car = Car("Honda", "Civic", 4)
car.display_car_info()
```
---

## 5. Polymorphism
Polymorphism means "many forms." In OOP, it refers to the ability to use a common interface for different data types. In Python, it can be achieved through method overriding or method overloading.

Example:
```python
class Bird:
    def sound(self):
        return "Tweet"

class Dog:
    def sound(self):
        return "Bark"

# Polymorphism in action:
animals = [Bird(), Dog()]

for animal in animals:
    print(animal.sound())  # Output: Tweet, Bark
```
---

## 6. Method Overriding
Method overriding occurs when a child class defines a method that has the same name as a method in the parent class. The child class's method overrides the parent's method.

Example:
```python
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

# Example usage:
dog = Dog()
print(dog.sound())  # Output: Bark
```
---

## 7. Method Overloading
Method overloading refers to defining multiple methods with the same name but different parameters. Python doesn't support traditional method overloading directly but can achieve similar results using default arguments.

Example:
```python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

# Example usage:
calc = Calculator()
print(calc.add(2, 3))  # Output: 5
print(calc.add(2, 3, 4))  # Output: 9
```
---

## 8. Constructors and Destructors
Constructor: The __init__() method is a special method in Python that is called when an object is instantiated. It initializes the object's attributes.
Destructor: The __del__() method is called when an object is about to be destroyed.
Example:
```python
class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is created")
    
    def __del__(self):
        print(f"{self.name} is destroyed")

# Example usage:
obj = MyClass("Object1")
del obj  # Output: Object1 is destroyed
```
---

### Summary of OOP Concepts:
* Classes and Objects: A class is a blueprint, and an object is an instance of a class.
* Encapsulation: Bundling data and methods into a class and restricting access to protect the data.
* Abstraction: Hiding complex details and showing only the essential parts.
* Inheritance: A way for one class to derive properties and methods from another class.
* Polymorphism: The ability to use a single interface for different data types.
* Method Overriding: A child class redefines a parent class method.
* Method Overloading: Defining methods with the same name but different signatures (achieved with default parameters in Python).
* Constructors and Destructors: Special methods to initialize and clean up objects.
* OOP concepts help in writing more modular, reusable, and maintainable code in Python.