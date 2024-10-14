# Advanced OOP Concepts in Python
## 1. Multiple Inheritance
Multiple inheritance is a feature of OOP where a class can inherit from more than one base class. This allows a class to inherit attributes and methods from multiple classes.

Example:
```python
class A:
    def method_A(self):
        print("Method A")

class B:
    def method_B(self):
        print("Method B")

class C(A, B):  # Multiple Inheritance
    def method_C(self):
        print("Method C")

# Example usage:
obj = C()
obj.method_A()  # Output: Method A
obj.method_B()  # Output: Method B
obj.method_C()  # Output: Method C
```
### Pros:
* Reuse functionality from multiple classes.
### Cons:
* Can lead to complexity, especially with the diamond problem, where two classes inherit from the same base class, causing ambiguity.
---

## 2. MRO (Method Resolution Order)
The Method Resolution Order (MRO) defines the order in which Python looks for methods in the hierarchy of classes, especially in the case of multiple inheritance.

* Python uses the C3 Linearization Algorithm for MRO.
* You can view the MRO by using the mro() method or __mro__ attribute.
Example:
```python
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    pass

# Example usage:
obj = D()
obj.method()  # Output: B method
print(D.mro())  # Shows the MRO: [D, B, C, A, object]
```
### Explanation:
Python resolves the method in the order [D, B, C, A, object].

---

## 3. Abstract Base Classes (ABCs)
Abstract Base Classes (ABCs) provide a way to define interfaces in Python. They are a part of the abc module. An abstract class cannot be instantiated and requires child classes to implement the abstract methods.

Example:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Example usage:
circle = Circle(5)
print(circle.area())  # Output: 78.5
print(circle.perimeter())  # Output: 31.400000000000002
```
### Use case:
* ABCs are useful for defining common interfaces or contracts in complex systems.


---
## 4. Interfaces vs Abstract Classes
An interface is a type of abstract class that only defines method signatures without any implementation, whereas an abstract class can define some methods and require child classes to implement the rest.

* Abstract classes: May have both abstract and concrete methods.
* Interfaces: Usually contain only abstract methods (in languages like Java), but in Python, this is emulated using ABCs.

---
## 5. Composition vs Inheritance
Inheritance: A class derives attributes and methods from a parent class.
* Composition: A class contains objects of other classes (has-a relationship).
* Composition is often preferred over inheritance because it promotes flexibility and reduces tight coupling between classes.

Example (Composition):
```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        self.engine.start()

# Example usage:
car = Car()
car.start()  # Output: Engine started
```

### Use case:
* Inheritance: Use when classes share a strong "is-a" relationship.
* Composition: Use when you want to include behaviors from other classes without a hierarchical relationship.
---

## 6. Mixins
A Mixin is a type of class used to "mix" additional functionality into a class without creating a deep inheritance hierarchy. Mixins allow you to add methods to multiple classes without directly inheriting from them.

Example:
```python
class LoggerMixin:
    def log(self, message):
        print(f"Log: {message}")

class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle, LoggerMixin):  # Inherit from both
    def start(self):
        super().start()
        self.log("Car has started")

# Example usage:
car = Car()
car.start()
```

### Use case:
* Mixins are useful for adding reusable functionality across classes (e.g., logging, validation, etc.).

---
## 7. Operator Overloading
Operator overloading allows you to define or modify the behavior of operators (e.g., +, -, *) for user-defined types (classes). This is done by defining special methods like ```__add__()```, ```__sub__()```, etc.

Example:
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Example usage:
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: Point(4, 6)
```
###  Use case:
* Operator overloading makes your custom objects behave like built-in types.

---
## 8. Property Decorators (Getters and Setters)
In Python, you can use the @property decorator to define getter, setter, and deleter methods, allowing you to manage access to instance variables in a controlled manner.

Example:
```python
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

# Example usage:
emp = Employee("John", 5000)
print(emp.salary)  # Output: 5000
emp.salary = 6000  # Updates the salary
```
### Use case:
* Property decorators are useful for encapsulating data with validation logic, preventing direct access to internal attributes.
---

## 9. Metaclasses
A metaclass is the class of a class. It defines how classes behave. You can create classes using a metaclass, and it can control how a class is constructed and initialized.

Example:
```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

# Example usage:
obj = MyClass()  # Output: Creating class: MyClass
```
### Use case:
* Metaclasses are useful for creating frameworks or libraries that need to control how classes are defined.

---
## 10. Duck Typing
Duck Typing is a concept where the type or class of an object is less important than the methods or behaviors it defines. In Python, you don't need to check the type of the object, but just call the methods it supports.

Example:
```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def make_it_fly(obj):
    obj.fly()

# Example usage:
bird = Bird()
plane = Airplane()
make_it_fly(bird)    # Output: Bird is flying
make_it_fly(plane)   # Output: Airplane is flying
```
### Use case:
* Duck typing is a hallmark of Python's dynamic typing, and it allows greater flexibility in function and class design.

### Conclusion
* These advanced OOP concepts in Python provide additional control, flexibility, and power when designing complex systems. Mastering these concepts will help us write more maintainable and scalable applications.

### Summary of Advanced Concepts:
* **Multiple Inheritance**: A class can inherit from multiple classes.
* **MRO**: Defines the order in which Python looks for methods in a class hierarchy.
* **Abstract Base Classes (ABCs)**: Define abstract methods that must be implemented in derived classes.
* **Composition vs Inheritance**: Composition provides more flexibility than inheritance.
* **Mixins**: Used to add functionality to classes without inheritance.
* **Operator** Overloading: Allows operators to be used with user-defined types.
* **Property Decorators**: Used to control access to instance variables.
* **Metaclasses**: Allow customization of class creation.
* **Duck Typing**: Objects are judged by the methods they provide, not their types.