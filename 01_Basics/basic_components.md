# 🔰 Basic Components of Python

---

### 1. Keywords
Keywords are reserved words that have special meaning and purpose in Python. They cannot be used as identifiers (variable names, function names, etc.).

**Trick:** To see a list of all Python keywords in your current version:
```python
import keyword
print(keyword.kwlist)
```
Examples: `if`, `else`, `for`, `while`, `break`, `continue`, `True`, `False`, `None`, `def`, `class`, `import`, `from`, `as`, `try`, `except`, `finally`, `with`, `return`, `yield`, `lambda`, `and`, `or`, `not`, `in`, `is`, `del`, `global`, `nonlocal`, `pass`, `assert`, `async`, `await`.

### 2. Operators
Operators are special symbols that perform operations on one or more operands.

**Easy Way to Remember Operators (Mnemonic: A L A R M B I)**

| Letter | Operator Type      | Description                                     | Examples                                     |
| :----- | :----------------- | :---------------------------------------------- | :------------------------------------------- |
| **A**  | Arithmetic         | Mathematical operations                         | `+`, `-`, `*`, `/`, `//` (floor div), `%`, `**` |
| **L**  | Logical            | Combine conditional statements                  | `and`, `or`, `not`                           |
| **A**  | Assignment         | Assign values to variables                      | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=` |
| **R**  | Relational         | Compare two values (return `True`/`False`)    | `==`, `!=`, `>`, `<`, `>=`, `<=`            |
| **M**  | Membership         | Test if a sequence contains a value             | `in`, `not in`                               |
| **B**  | Bitwise            | Operate on bits (binary representation)         | `&`, `|`, `^`, `~`, `<<`, `>>`               |
| **I**  | Identity           | Compare memory locations of two objects         | `is`, `is not`                               |

**Examples:**
```python
a = 10
b = 3

# Arithmetic
print(f"a + b = {a + b}")   # 13
print(f"a / b = {a / b}")   # 3.333... (float division)
print(f"a // b = {a // b}") # 3 (floor division)
print(f"a % b = {a % b}")   # 1 (remainder)

# Assignment
c = a + b # c becomes 13
c += 5    # c becomes 18 (c = c + 5)

# Relational
print(f"a == b is {a == b}") # False
print(f"a > b is {a > b}")   # True

# Logical
x = True
y = False
print(f"x and y is {x and y}") # False
print(f"x or y is {x or y}")  # True

# Membership
my_list = [1, 2, 3, 4, 5]
print(f"1 in my_list is {1 in my_list}")     # True
print(f"5 not in my_list is {5 not in my_list}") # True

# Identity (compares memory addresses, not just values)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 is list2 is {list1 is list2}") # False (different objects in memory)
print(f"list1 is list3 is {list1 is list3}") # True (list3 refers to the same object as list1)
```

### 3. Built-in Functions
These are functions that are always available for use without needing to import any modules. Python provides a rich set of built-in functions for common tasks.

Examples:
*   `print()` – Outputs data to the console.
*   `input()` – Reads input from the user.
*   `type()` – Returns the type of an object.
    ```python
    print(type(10))      # <class 'int'>
    print(type("hello")) # <class 'str'>
    ```
*   `id()` – Returns the identity (memory address) of an object.
    ```python
    num = 10
    print(id(num))
    ```
*   `len()` – Returns the length (number of items) of an object.
    ```python
    print(len("Python")) # 6
    print(len([1, 2, 3])) # 3
    ```
*   `range()` – Generates a sequence of numbers.
*   `int()`, `float()`, `str()`, `bool()` – Type conversion functions.
*   `min()`, `max()`, `sum()` – For numerical operations on iterables.
*   `abs()` – Absolute value.
*   `round()` – Rounds a number.

### 4. Library Functions (Module Functions)
Functions provided by modules (libraries) that need to be explicitly imported before use.

Examples:
```python
import math
print(math.sqrt(16)) # 4.0

import random
print(random.randint(1, 10)) # A random integer between 1 and 10 (inclusive)

import os
print(os.getcwd()) # Get current working directory

from datetime import datetime
print(datetime.now()) # Current date and time
```
**Point to Remember:** Always import the necessary module or specific functions/classes from a module before using them.
