<div align="center">
<h1> DAY 1 <br> Python Basics</h1>

</div>

## Table of Content
- [DataTypes](#datatypes)
  - [1. Integer](#1-integer)
  - [2. Float](#2-float)
  - [3. String](#3-string)
  - [4. Tuple](#4-tuple)
  - [5. List](#5-list)
  - [6. Dictionary](#6-dictionary)
  - [7. Set](#7-set)
  - [8. Boolean Data Type:](#8-boolean-data-type)
  - [9. None Data Type](#9-none-data-type)
- [List Operation](#list-operation)
  - [Creating List](#creating-list)
  - [Accessing Element](#accessing-element)
  - [Modifyin Elements:](#modifyin-elements)
  - [Removing Elements:](#removing-elements)
  - [Other Operations:](#other-operations)
    - [Examples:](#examples)
- [Set Operations](#set-operations)
  - [Creating a Set:](#creating-a-set)
  - [Adding Elements:](#adding-elements)
  - [Removing Elements:](#removing-elements-1)
  - [Union of Sets:](#union-of-sets)
  - [Intersection of Sets:](#intersection-of-sets)
  - [Difference of Sets:](#difference-of-sets)
  - [Symmetric Difference of Sets:](#symmetric-difference-of-sets)
  - [Checking Subsets and Supersets:](#checking-subsets-and-supersets)
  - [Updating Sets:](#updating-sets)
    - [Example:](#example)
- [Dictionary Operation](#dictionary-operation)
  - [Creating a Dictionary:](#creating-a-dictionary)
  - [Accessing Values:](#accessing-values)
  - [Modifying Values:](#modifying-values)
  - [Adding New Key-Value Pairs:](#adding-new-key-value-pairs)
  - [Checking if a Key Exists:](#checking-if-a-key-exists)
  - [Deleting Key-Value Pairs:](#deleting-key-value-pairs)
  - [Getting All Keys:](#getting-all-keys)
  - [Getting All Values:](#getting-all-values)
  - [Getting All Key-Value Pairs:](#getting-all-key-value-pairs)
  - [Iterating Over Key-Value Pairs:](#iterating-over-key-value-pairs)
  - [Additional Operations:](#additional-operations)
  - [Merging Dictionaries:](#merging-dictionaries)
    - [Unpacking Method](#unpacking-method)
    - [Updating Values:](#updating-values)
    - [Clearing a Dictionary:](#clearing-a-dictionary)
    - [Copying a Dictionary:](#copying-a-dictionary)
    - [Example:](#example-1)
- [Tuple Operations](#tuple-operations)
  - [Creating a Tuple:](#creating-a-tuple)
  - [Accessing Elements:](#accessing-elements)
  - [Slicing:](#slicing)
  - [Packing and Unpacking:](#packing-and-unpacking)
    - [Packing:](#packing)
    - [Unpacking:](#unpacking)
    - [Note:](#note)
    - [Example:](#example-2)
    - [Additional Notes:](#additional-notes)
- [String Operation](#string-operation)
  - [Creating a String:](#creating-a-string)
  - [Accessing Characters:](#accessing-characters)
  - [Slicing:](#slicing-1)
  - [Concatenation:](#concatenation)
  - [Repetition:](#repetition)
  - [Membership Testing:](#membership-testing)
  - [Length:](#length)
  - [String Methods:](#string-methods)
    - [Example:](#example-3)
- [Differnet Type of Loop Functions](#differnet-type-of-loop-functions)
  - [1. for Loop:](#1-for-loop)
  - [2. while Loop:](#2-while-loop)
  - [3. do-while Loop (Using while True):](#3-do-while-loop-using-while-true)
  - [4. Nested Loops:](#4-nested-loops)

# DataTypes
## 1. Integer
* Represents whole numbers without decimal points.
* Can be positive, negative, or zero.
    Examples:
  
<h3> Python Code :</h3>
    ```python
        a=5
    ```

## 2. Float
* Represents numbers with decimal points.
* Can be positive, negative, or zero.

    Examples:
<h3> Python Code :</h3> 

    ```python
        b=5.123
    ```

## 3. String
* Ordered, immutable sequence of characters.
* Supports indexing, slicing, and various string methods.

    Example:
<h3> Python Code :</h3>  

    ```python
        a="hello world"
    ```

## 4. Tuple
* Ordered, immutable collection of elements.
* Elements can be of any data type.
* Supports indexing and slicing.

    Example :
<h3> Python Code :</h3>  
  
    ```python
        my_tuple = (1,2,3,4,5,6)
    ```



## 5. List
* Ordered, mutable collection of elements.
* Elements can be of any data type.
* Supports indexing, slicing, and various methods.

    Example :
<h3> Python Code :</h3>  

    ```python
        my_list = [5,6,7,8,9]
    ```
## 6. Dictionary
* Used to store data values in key:value pairs
* Ordered collection of key-value pairs.(Earlier it was unordered > 3.6)
* Dictionary is mutable but Keys must be unique and immutable.
* Values can be of any data type.
* Access values using keys.

    Example :
<h3> Python Code :</h3>

    ```python
        my_dict = {
            'a':1,
            1:'ABC',
            'prize:1.234
        }
    ```


## 7. Set
* Unordered collection of unique elements.
* Elements cannot be duplicated.
* Supports set operations like union, intersection, difference, and symmetric difference.
* Mutable
  
    Example :
<h3> Python Code :</h3>  

    ```python
        my_set = {4,5,6,7,}
    ```

## 8. Boolean Data Type:
* Represents ```True``` or ```False``` values.
* Used for logical operations and conditional statements

    Example:
<h3> Python Code :</h3>  

    ```python
        is_valid = True
    ```

## 9. None Data Type
* Represents the absence of a value.
* Often used as a default value or to indicate that a function returns no value.
 
    Example:
<h3> Python Code :</h3>  

    ```python
        result = None
    ```

---

# List Operation
## Creating List
* Empty list: ```my_list = []```
* List with elements: ```my_list = [1, 2, 3, "hello"]```
  
## Accessing Element
* Indexing: ```element = my_list[index]```
* Slicing: ```sublist = my_list[start:end:step]```

## Modifyin Elements:
* Assignment: ```my_list[index] = new_value```
* Append: ```my_list.append(element)```
* Insert: ```my_list.insert(index, element)```
* Extend: ```my_list.extend(another_list)```

## Removing Elements:
* Pop: ```removed_element = my_list.pop(index)```
* Remove: ```my_list.remove(element)```
* Delete: ```del my_list[index]```

## Other Operations:

* Length: ```length = len(my_list)```
* Membership: ```is_in = element in my_list```
* Reversing: ```my_list.reverse()```
* Sorting: ```my_list.sort()```
* Copying: ```new_list = my_list.copy()```
* Concatenation: ```combined_list = list1 + list2*```

### Examples:
<h3> Python Code :</h3>

```python
    my_list = [1, 2, 3, "hello"]

    # Accessing elements
    first_element = my_list[0]  # Output: 1
    sublist = my_list[1:3]      # Output: [2, 3]

    # Modifying elements
    my_list[2] = 4
    my_list.append(5)
    my_list.insert(1, "world")

    # Removing elements
    removed_element = my_list.pop()
    my_list.remove(3)
    del my_list[0]

    # Other operations
    length = len(my_list)
    is_in = 2 in my_list
    my_list.reverse()
    my_list.sort()
    new_list = my_list.copy()
    combined_list = my_list + [6, 7]

    print(my_list)  # Output: ['world', 2, 4, 5, 6, 7]
```

---
# Set Operations

Sets in Python are unordered collections of unique elements. They are useful for performing various mathematical operations on sets.

## Creating a Set:
<h3> Python Code :</h3>

```python
    my_set = {1, 2, 3, 4}
```

## Adding Elements:
<h3> Python Code :</h3>


```python
    my_set.add(5)
```

## Removing Elements:
<h3> Python Code :</h3>


```python
    my_set.remove(3)  # Raises KeyError if element not found
    my_set.discard(6)  # Does not raise error if element not found
```

## Union of Sets:
<h3> Python Code :</h3>


```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union_set = set1.union(set2)  # Or set1 | set2
```

## Intersection of Sets:
<h3> Python Code :</h3>


```python
    intersection_set = set1.intersection(set2)  # Or set1 & set2
```

## Difference of Sets:
<h3> Python Code :</h3>

```python
    difference_set = set1.difference(set2)  # Or set1 - set2
```

## Symmetric Difference of Sets:
<h3> Python Code :</h3>

```python
    symmetric_difference_set = set1.symmetric_difference(set2)  # Or set1 ^ set2
```

## Checking Subsets and Supersets:
<h3> Python Code :</h3>

```python
    is_subset = set1.issubset(set2)
    is_superset = set1.issuperset(set2)
```

## Updating Sets:
<h3> Python Code :</h3>

```python
    set1.update(set2)  # Equivalent to union and assignment
    set1.intersection_update(set2)  # Equivalent to intersection and assignment
    set1.difference_update(set2)  # Equivalent to difference and assignment
    set1.symmetric_difference_update(set2)  # Equivalent to symmetric difference and assignment
```

### Example:
<h3> Python Code :</h3>

```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    # Union
    union_set = set1.union(set2)
    print(union_set)  # Output: {1, 2, 3, 4, 5}

    # Intersection
    intersection_set = set1.intersection(set2)
    print(intersection_set)  # Output: {3}

    # Difference
    difference_set   
    = set1.difference(set2)
    print(difference_set)  # Output:   
    {1, 2}

    # Symmetric Difference
    symmetric_difference_set = set1.symmetric_difference(set2)
    print(symmetric_difference_set)  # Output: {1, 2, 4,5}

    # Check Subset
    is_subset = set1.issubset(set2)
    print(is_subset)  # Output: False

    # Check Superset
    is_superset = set1.issuperset(set2)
    print(is_superset)  # Output: False
```

---
# Dictionary Operation
## Creating a Dictionary:
<h3> Python Code :</h3>

```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
```

## Accessing Values:
<h3> Python Code :</h3>

```python
value = my_dict['key1']  # Accessing value by key
```

## Modifying Values:
<h3> Python Code :</h3>

```python
my_dict['key1'] = 'new_value'
```

## Adding New Key-Value Pairs:
<h3> Python Code :</h3>

```python
my_dict['key3'] = 'value3'
```

## Checking if a Key Exists:
<h3> Python Code :</h3>

```python
if 'key4' in my_dict:
    print("Key exists")
else:
    print("Key does not exist")
```

## Deleting Key-Value Pairs:
<h3> Python Code :</h3>

```python
del my_dict['key2']
```

## Getting All Keys:
<h3> Python Code :</h3>

```python
keys = my_dict.keys()
```

## Getting All Values:
<h3> Python Code :</h3>

```python
values = my_dict.values()
```

## Getting All Key-Value Pairs:
<h3> Python Code :</h3>

```python
items = my_dict.items()
```

## Iterating Over Key-Value Pairs:
<h3> Python Code :</h3>

```python
for key, value in my_dict.items():
    print(key, value)
```

## Additional Operations:

## Merging Dictionaries:
### Unpacking Method
<h3> Python Code :</h3>

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
```

### Updating Values:
<h3> Python Code :</h3>

```python
my_dict.update({'key1': 'updated_value'})
```

### Clearing a Dictionary:
<h3> Python Code :</h3>

```python
my_dict.clear()
```

### Copying a Dictionary:
<h3> Python Code :</h3>

```python
new_dict = my_dict.copy()
```

### Example:
<h3> Python Code :</h3>

```python
    my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

    print(my_dict['name'])  # Output: Alice
    my_dict['age'] = 31
    print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

    del my_dict['city']
    print(my_dict)  # Output: {'name': 'Alice', 'age': 31}

    for key, value in my_dict.items():
        print(key, value)
```

---
# Tuple Operations
## Creating a Tuple:
<h3> Python Code :</h3>

```python
my_tuple = (1, 2, 3, 4, 5)
```

## Accessing Elements:
<h3> Python Code :</h3>

```python
element = my_tuple[index]  # Accessing element by index
```

## Slicing:
<h3> Python Code :</h3>

```python
subtuple = my_tuple[start:end:step]
```

## Packing and Unpacking:
### Packing:
<h3> Python Code :</h3>

```python
values = 1, 2, 3
```


### Unpacking:
<h3> Python Code :</h3>

```python
a, b, c = values
```

### Note: 
Tuples are immutable, so you cannot modify their elements directly. However, you can create new tuples by combining existing tuples or using slicing.

### Example:
<h3> Python Code :</h3>

```python
    my_tuple = (1, 2, 3, 4, 5)

    # Accessing elements
    first_element = my_tuple[0]  # Output: 1
    subtuple = my_tuple[1:3]      # Output: (2, 3)

    # Packing and unpacking
    values = 10, 20, 30
    x, y, z = values

    # Creating a new tuple
    new_tuple = my_tuple + (6, 7)
    print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)
    Use code with caution.
```

### Additional Notes:

* Tuples can be used as keys in dictionaries because they are immutable.
* Tuples are often used to represent fixed-size data structures, such as coordinates or database records.
* The ```tuple() ```function can be used to convert other sequences (like lists) to tuples.

---
# String Operation
## Creating a String:
<h3> Python Code :</h3>

```python
my_string = "Hello, world!"
```

## Accessing Characters:
<h3> Python Code :</h3>

```python
char = my_string[index]  # Accessing character by index
```

## Slicing:
<h3> Python Code :</h3>

```python
substring = my_string[start:end:step]
```

## Concatenation:
<h3> Python Code :</h3>

```python
combined_string = string1 + string2
```

## Repetition:
<h3> Python Code :</h3>

```python
repeated_string = string * n
```

## Membership Testing:
<h3> Python Code :</h3>

```python
is_in = substring in string
```

## Length:
<h3> Python Code :</h3>

```python
length = len(string)
```

## String Methods:
```upper()```: Converts to uppercase.

```lower()```: Converts to lowercase.

```capitalize()```: Capitalizes the first letter

```title()```: Capitalizes the first letter of each word

```count(substring)```~: Counts occurrences of a substring

```find(substring)```: Finds the index of the first occurrence 
of a substring

```replace(old, new)```: Replaces occurrences of one substring 
with another

```split(separator)```: Splits the string into a list of 
substrings

```join(list)```: Joins elements of a list into a string

```strip()```: Removes leading and trailing whitespace

```lstrip()```: Removes leading whitespace

```rstrip()```: Removes trailing whitespace   


### Example:
<h3> Python Code :</h3>

```python
    my_string = "Hello, world!"

    # Accessing characters
    first_char = my_string[0]  # Output: H
    substring = my_string[7:12]  # Output: world

    # Concatenation and repetition
    combined_string = my_string + " How are you?"
    repeated_string = my_string * 3

    # Membership testing
    is_in = "world" in my_string

    # String methods
    uppercase_string = my_string.upper()

    lowercase_string = my_string.lower()
    capitalized_string = my_string.capitalize()
    count = my_string.count("o")
    index = my_string.find("world")
    new_string = my_string.replace("world", "everyone")
    split_list = my_string.split()
    joined_string = " ".join(split_list)
    stripped_string = my_string.strip()

    print(uppercase_string)  # Output: HELLO, WORLD!
    print(lowercase_string)  # Output: hello, world!
    print(capitalized_string)  # Output: Hello, world!
    print(count)  # Output: 3
    print(index)  # Output: 7
    print(new_string)  # Output: Hello, everyone!
    print(split_list)  # Output: ['Hello,', 'world!']
    print(joined_string)  # Output: Hello, world!
    print(stripped_string)  # Output: Hello, world!
```

---
# Differnet Type of Loop Functions
## 1. for Loop:

* Iterates over a sequence (list, tuple, string, dictionary, set, or range object).
* Executes a block of code for each element in the sequence.

Example:
<h3> Python Code :</h3>

```python
    # Iterating over a list
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    # Iterating over a range
    for i in range(5):   

        print(i)
```

## 2. while Loop:

* Executes a block of code as long as a specified condition is true.
* Useful for repeating actions until a certain condition is met.

Example:
<h3> Python Code :</h3>

```python
    count = 0
    while count < 5:
        print(count)
    count += 1
```

## 3. do-while Loop (Using while True):

* Executes a block of code at least once, then continues to execute as long as a specified condition is true.
* This is not a built-in construct in Python, but it can be simulated using a while True loop and a break statement.

Example:
<h3> Python Code :</h3>

```python
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
```

## 4. Nested Loops:

* Loops within loops.
* Useful for iterating over multiple sequences or performing nested operations.

Example:
<h3> Python Code :</h3>

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```
---
