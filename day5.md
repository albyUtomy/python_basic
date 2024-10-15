# Recursive Function: Factorial Example
A recursive function is a function that calls itself in order to solve a problem. In the case of a factorial, the function keeps calling itself with decremented values of the input until it reaches the base case.

## Factorial Definition
The factorial of a non-negative integer ```n``` is the product of all positive integers less than or equal to ```n```. It is denoted by ```n!```. The recursive formula for factorial is: ****n!=n×(n−1)!****
with the base case: ***0!=1***
## Recursive Factorial Function
```python
def factorial_r(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial_r(n - 1)
```

#### Example: Calculating Factorial of 5
Let’s calculate ```5!``` using the recursive function.


5!=5×4×3×2×1=120
When ```factorial_r(5)``` is called, the function will proceed as follows:

```factorial_r(5)``` returns ```5 * factorial_r(4)```

```factorial_r(4)``` returns ```4 * factorial_r(3)```

```factorial_r(3) ```returns ```3 * factorial_r(2)```

```factorial_r(2)``` returns ```2 * factorial_r(1)```

```factorial_r(1)``` returns ```1``` (base case)

Then, the results are multiplied together:

5×4×3×2×1=120
So, ```factorial_r(5)``` returns ```120```.