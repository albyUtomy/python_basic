<div align="center">

# DAY 3

</div>

# Python Concepts
## 1. List Comprehension
List comprehension provides a concise way to create lists. It consists of brackets containing an expression followed by a for clause, and zero or more if clauses.

### Syntax:
```python
[expression for item in iterable if condition]
```
### Example:
```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
### Benefits:
* More readable and concise compared to loops.
* Efficient and faster.

## 2. Dictionary Comprehension
Dictionary comprehension is used to create dictionaries from an iterable in a single line of code.

### Syntax:
```python
{key_expression: value_expression for item in iterable if condition}
```
### Example:
```python
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```
### Benefits:
* Reduces the code length and improves readability.
* Efficient in creating large dictionaries.

## 3. Backtracking Algorithm
Backtracking is a general algorithm for finding solutions to computational problems by trying partial solutions and then abandoning them if they are not suitable (i.e., "backtracking").

### Steps:
* Choose a possible solution path.
* Recursively explore the path.
* If the current path leads to a solution, return the solution.
* If the path does not lead to a solution, backtrack and try another path.
### Example (Solving the N-Queens problem):
```python
def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True

    def solve(board, col):
        if col >= n:
            return True
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                if solve(board, col + 1):
                    return True
                board[i][col] = '.'
        return False

    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return board

n = 4
solution = solve_n_queens(n)
for row in solution:
    print(" ".join(row))
```


## 4. Decorator
A decorator is a function in Python that allows you to modify the behavior of another function or class. Decorators are often used for logging, enforcing access control, instrumentation, etc.

### Syntax:
```python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Add extra functionality
        return original_function(*args, **kwargs)
    return wrapper_function
```
### Example:
```python
def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before the function.
# Hello!
# Something after the function.

```
### Benefits:
* Can easily modify the behavior of a function without modifying the actual function.
* Helps in cross-cutting concerns like logging, authentication, and caching