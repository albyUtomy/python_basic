
<div align="center">

# DAY 5

</div>

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

---
# Integer to Roman Numeral Conversion

This project implements a Python function to convert an integer to a Roman numeral. The function works by mapping specific integer values to their corresponding Roman numeral symbols and building the Roman numeral string from the largest values to the smallest.

## Logic

1. **Roman Numeral Symbols:**
   - Roman numerals are represented using the following symbols:
     - `I = 1`, `V = 5`, `X = 10`, `L = 50`, `C = 100`, `D = 500`, `M = 1000`
   - Additionally, certain combinations are used to represent numbers in a "subtractive" form:
     - `IV = 4`, `IX = 9`, `XL = 40`, `XC = 90`, `CD = 400`, `CM = 900`

2. **Approach:**
   - The function uses a dictionary (hashtable) to map integers to their Roman numeral symbols.
   - It iterates through this dictionary from the largest to the smallest value.
   - For each value, it checks how many times it fits into the input number, appends the corresponding Roman symbol, and subtracts that value from the number.
   - The process continues until the input number becomes 0.

3. **Efficiency:**
   - The algorithm works in constant time, as the list of Roman numerals is fixed and doesn’t depend on the size of the input number.

## Python Program

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of integer values to Roman numeral symbols
        roman_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }

        roman = ""
        
        # Iterate over the dictionary in decreasing order of values
        for value, symbol in roman_map.items():
            # Find how many times the current value fits into num
            count = num // value
            # Subtract the corresponding value
            num -= count * value
            # Append the Roman numeral symbol
            roman += symbol * count
        
        return roman

# Example usage
obj = Solution()
print(obj.intToRoman(1994))  # Output: MCMXCIV
```