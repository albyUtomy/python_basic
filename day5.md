
<div align="center">

# DAY 5
# Python Algorithmic Solutions
</div>

## Table of Content
- [DAY 5](#day-5)
- [Python Algorithmic Solutions](#python-algorithmic-solutions)
  - [Table of Content](#table-of-content)
- [1. Recursive Function: Factorial Example](#1-recursive-function-factorial-example)
  - [Factorial Definition](#factorial-definition)
  - [Recursive Factorial Function](#recursive-factorial-function)
      - [Example: Calculating Factorial of 5](#example-calculating-factorial-of-5)
- [2. Integer to Roman Numeral Conversion](#2-integer-to-roman-numeral-conversion)
  - [Logic](#logic)
  - [Python Program](#python-program)
- [3. Rotate Array](#3-rotate-array)
    - [Problem:](#problem)
    - [Solution Approach:](#solution-approach)
    - [Code:](#code)
    - [Usage:](#usage)
- [4. Reverse Words in a String](#4-reverse-words-in-a-string)
    - [Problem:](#problem-1)
    - [Solution Approach:](#solution-approach-1)
    - [Usage:](#usage-1)
- [5. Remove Duplicates from Sorted Array II](#5-remove-duplicates-from-sorted-array-ii)
    - [Problem:](#problem-2)
    - [Solution Approach:](#solution-approach-2)
    - [Usage:](#usage-2)
- [6. Best Time to Buy and Sell Stock](#6-best-time-to-buy-and-sell-stock)
    - [Problem:](#problem-3)
    - [Solution Approach:](#solution-approach-3)
    - [Code:](#code-1)
    - [Usage:](#usage-3)
- [7. Best Time to Buy and Sell Stock II](#7-best-time-to-buy-and-sell-stock-ii)
    - [Problem:](#problem-4)
    - [Solution Approach:](#solution-approach-4)
    - [Usage:](#usage-4)


# 1. Recursive Function: Factorial Example
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
# 2. Integer to Roman Numeral Conversion

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

---
# 3. Rotate Array
### Problem:
Given an array, rotate it to the right by k steps, where k is non-negative.

### Solution Approach:

* Reverse the entire array.
* Reverse the first k elements.
* Reverse the rest of the array.

### Code:

```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        print(nums)
```
### Usage:

```python
obj = Solution()
List2 = [1, 2, 3, 4, 5, 6, 7]
obj.rotate(List2, 5)  # Output: [3, 4, 5, 6, 7, 1, 2]
```


---
# 4. Reverse Words in a String
### Problem:
Given a string, reverse the order of the words.

### Solution Approach:
* Split the string into words, reverse the list of words, and join them back into a single string.

Code:

```python
def reverseWords(s: str) -> str:
    str_lst = [word for word in s.split()]
    reversed_list = str_lst[::-1]
    return ' '.join(reversed_list)
```
### Usage:

```python
print(reverseWords("Happy Birthday to you"))  # Output: "you to Birthday Happy"
```

---
# 5. Remove Duplicates from Sorted Array II
### Problem:
Remove duplicates from a sorted array where each element can appear at most twice.

### Solution Approach:
* Iterate through the array, ensuring no element appears more than twice. Elements are shifted in-place.

Code:

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        insert_position = 2
        result = []
        
        for i in range(2, len(nums)):
            if nums[i] != nums[insert_position - 2]:
                nums[insert_position] = nums[i]
                result.append(nums[insert_position])
                insert_position += 1
        

        return result
```
### Usage:

```python
obj = Solution()
print(obj.removeDuplicates([0, 0, 1, 1, 1, 1, 4, 4, 2, 3, 3]))  # Output: [0, 0, 1, 1, 4, 4, 2, 3]
```

---

# 6. Best Time to Buy and Sell Stock
### Problem:
Find the maximum profit you can achieve from one transaction (buy one day and sell on another day).

### Solution Approach:
* Track the lowest price so far, and compute the potential profit by subtracting the lowest price from the current price.

### Code:

```python
def maxProfit(prices) -> int:
    if not prices:
        return 0

    lowest_price = prices[0]
    max_profit = 0

    for price in prices:
        lowest_price = min(lowest_price, price)
        max_profit = max(max_profit, price - lowest_price)

    return max_profit
```
### Usage:

```python
List_p = [2, 3, 7, 1, 6, 7, 8, 9]
print(maxProfit(List_p))  # Output: 8
```
---

# 7. Best Time to Buy and Sell Stock II
### Problem:
Find the maximum profit you can achieve from multiple transactions (buying and selling on different days, multiple times).

### Solution Approach:
* If the price on the next day is higher than the current day, calculate the profit and add it to the total.

Code:

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
```
### Usage:

```python
obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 7
print(obj.maxProfit([1, 2, 3, 4, 5]))    # Output: 4
print(obj.maxProfit([7, 6, 4, 3, 1]))    # Output: 0
```