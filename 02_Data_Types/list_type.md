# Lists in Python (`list`)

A **List** is a versatile, **mutable** collection of items. It is ordered, meaning items maintain their position, and allows duplicate elements. Lists are one of the most commonly used data types in Python, fundamental for storing sequences of data.

---

## 1. Characteristics
*   **Ordered**: Items maintain their position.
*   **Mutable**: You can change, add, or remove items after creation.
*   **Heterogeneous**: Can hold mixed data types (int, str, float, etc.).
*   **Allow Duplicates**: `[1, 1, 2]` is valid.

---

## 2. List Creation
Lists are defined using square brackets `[]`.
**Syntax**: `[item1, item2, ...]`

```python
l = [10, 20, 30, "Hello", 3.14]
empty_list = []
mixed_list = ["apple", 1, True, 3.14]
```

---

## 3. Indexing and Slicing
Lists support indexing and slicing just like strings.

*   **Positive Indexing**: Starts from `0` (Left to Right).
*   **Negative Indexing**: Starts from `-1` (Right to Left).
*   **Slicing Syntax**: `list[start : end : step]`

```python
a = [10, 20, 30, 40, 50]

# Indexing
print(a[0])    # 10
print(a[-1])   # 50

# Slicing
print(a[1:4])  # [20, 30, 40]
# Explanation: Starts at index 1 (20), up to but not including index 4 (50).

print(a[-4:-1]) # [20, 30, 40]
# Explanation: Starts at -4 (20), goes to -1 (50, exclusive).

# Reverse a list using slicing
print(a[::-1]) # [50, 40, 30, 20, 10]
```

---

## 4. Nested Lists
A list can contain other lists or complex data structures.

```python
# List containing INT, Float tuple, and Set
s5 = [10, 20, (100, 200, 'Hello'), {1, 2, 3}]

# Accessing Nested Elements
# Fetch 100
print(s5[2][0])  # 100
# s5[2] is (100, 200, 'Hello')
# [0] refers to the first item of that tuple.

# Fetch 200
print(s5[2][1])  # 200

# Deeply Nested Example
l6 = [1, 2.2, [2+2j, True, ['Yadav ji', 'Pandey Ji', False]]]

# Access 'Pandey Ji'
print(l6[2][2][1])   # 'Pandey Ji'

# Using Negative Indexing for the same:
print(l6[-1][-1][-2]) # 'Pandey Ji'
```

---

## 5. Common List Methods

| Method | Description | Example |
| :--- | :--- | :--- |
| `append(item)` | Adds a single `item` to the end. | `my_list.append(5)` |
| `extend(iterable)` | Adds all elements from an `iterable` to the end. | `my_list.extend([6, 7])` |
| `insert(index, item)` | Inserts `item` at a specified `index`. | `my_list.insert(1, 1.5)` |
| `remove(value)` | Removes the first occurrence of `value`. | `my_list.remove(2)` |
| `pop(index=-1)` | Removes and returns the item at `index` (default last). | `last_item = my_list.pop()` |
| `clear()` | Removes all items from the list. | `my_list.clear()` |
| `index(value, start, end)` | Returns the index of the first `value`. | `my_list.index(3)` |
| `count(value)` | Returns the number of occurrences of `value`. | `my_list.count(1)` |
| `sort(reverse=False)` | Sorts the list in-place. | `my_list.sort()` |
| `reverse()` | Reverses the order of elements in-place. | `my_list.reverse()` |
| `copy()` | Returns a shallow copy of the list. | `new_list = my_list.copy()` |
| `len(list)` | (Built-in function) Returns the number of items. | `len(my_list)` |
| `max(list)` | (Built-in function) Returns the largest item. | `max(my_list)` |
| `min(list)` | (Built-in function) Returns the smallest item. | `min(my_list)` |
| `sum(list)` | (Built-in function) Returns the sum of items (numeric). | `sum(my_list)` |

---

## 6. List Copying: Reference vs Shallow vs Deep Copy
Understanding how Python copies lists is critical for avoiding bugs, especially with nested data.

### 6.1. Reference Copy (Assignment `=`)
When you assign one list to another using `=`, you are creating a new reference (alias) to the **same** memory location. Changes in one affect the other.

```python
L = [10, 20, 30]
a = L         # 'a' points to the same object as 'L'

a[0] = 99     # Modifying 'a' changes 'L' too!

print(L)      # [99, 20, 30]
print(a)      # [99, 20, 30]
```

### 6.2. Shallow Copy (`.copy()` or `[:]`)
A shallow copy creates a **new** outer list. For simple (flat) lists, this makes them independent. However, for nested lists, it only copies the *references* to the inner lists, meaning the inner lists are **shared**.

```python
l2 = [1, 2, 3, [3, 4], 7]
l4 = l2.copy() # or l4 = l2[:]

# Modifying the inner list affects BOTH
l4[3][0] = 999 

print(l2) # [1, 2, 3, [999, 4], 7] (Original changed!)
print(l4) # [1, 2, 3, [999, 4], 7]
# "Inside nested list does affect both values"
```

### 6.3. Deep Copy (`copy.deepcopy()`)
A deep copy creates a completely independent clone of the original object and **recursively** copies all nested objects.

```python
import copy

l = [10, 20, [30, 40]]
y = copy.deepcopy(l) # Creates fully independent copy

# Modify original
l[2][0] = 77

print(l) # [10, 20, [77, 40]]
print(y) # [10, 20, [30, 40]]
# "In this both become independent"
```

### 📊 Copying Summary Table

| Type | Syntax | Outer Level | Nested Level |
| :--- | :--- | :--- | :--- |
| **Reference** | `a = b` | Same | Same |
| **Shallow** | `b.copy()` | New | Same (Shared) |
| **Deep** | `copy.deepcopy(b)` | New | New (Independent) |

> **Exam & Interview Gold**: Understanding how Python copies lists is critical for avoiding bugs in nested data. Remember: Shallow copy creates a new outer shell, but inner elements are shared references.

---

## 7. Looping Through a List

```python
my_list = ['apple', 'banana', 'cherry']

# Basic for loop
for item in my_list:
    print(item)

# Looping with index using range(len())
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")

# Looping with index and value using enumerate()
for index, value in enumerate(my_list):
    print(f"Index {index}: {value}")

# Reverse loop
for item in reversed(my_list):
    print(item)
```

---

## 🎯 VVI Interview Questions & Tricks

### Q1. What is the difference between `append()` and `extend()` for lists?
*   `append(item)`: Adds a single `item` to the end of the list. The `item` can be any data type, including another list (which will be added as a single element).
    ```python
    a = [1, 2]
    a.append([3, 4]) # a becomes [1, 2, [3, 4]]
    ```
*   `extend(iterable)`: Adds all elements from an `iterable` (like another list, tuple, or string) to the end of the list. It "extends" the list by adding each element individually.
    ```python
    a = [1, 2]
    a.extend([3, 4]) # a becomes [1, 2, 3, 4]
    ```

### Q2. How can you remove duplicates from a list?
**Trick:** Convert the list to a set (which automatically handles uniqueness) and then convert it back to a list. Note that this method does **not** preserve the original order.
```python
my_list = [1, 2, 2, 3]
unique_list = list(set(my_list))
print(unique_list) # Output: [1, 2, 3] (order might vary)
```
To preserve order, you can use `dict.fromkeys()` (Python 3.7+):
```python
my_list = [1, 2, 2, 3]
unique_ordered_list = list(dict.fromkeys(my_list))
print(unique_ordered_list) # Output: [1, 2, 3]
```

### Q3. Explain `==` vs `is` when comparing lists.
*   `==` (Equality operator): Compares the **values** (content) of the lists. It returns `True` if both lists contain the same elements in the same order.
*   `is` (Identity operator): Compares the **memory addresses** (references) of the lists. It returns `True` only if both variables point to the exact same list object in memory.

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2) # True (Values are equal)
print(list1 is list2) # False (Different objects in memory)
print(list1 is list3) # True (Same object in memory)
```

### Q4. What is the `*` operator trap with nested lists?
When creating nested lists using the `*` operator, all inner lists refer to the **same memory object**. Modifying one inner list will affect all of them.

```python
a = [[1, 2]]*3
a[0][0] = 9
print(a)
# Output: [[9, 2], [9, 2], [9, 2]]
# All inner lists changed because they are references to the same list.
```
**Fix:** Use a list comprehension to create independent inner lists.
```python
a = [[1, 2] for _ in range(3)]
a[0][0] = 9
print(a)
# Output: [[9, 2], [1, 2], [1, 2]]
```

### Q5. What happens if you modify a list while iterating over it?
Modifying a list (e.g., adding or removing elements) while iterating over it using a `for` loop can lead to unexpected behavior, such as skipping elements or infinite loops.

```python
nums = [1, 2, 3, 4]
for x in nums:
    if x % 2 == 0:
        nums.remove(x)
print(nums)
# Output: [1, 3] (Element 2 was removed, then 3 was skipped because 4 moved to index 2)
```
**Fix:** Iterate over a copy of the list, or use a list comprehension to create a new list.
```python
# Iterate over a copy
nums = [1, 2, 3, 4]
for x in nums[:]: # Iterate over a shallow copy
    if x % 2 == 0:
        nums.remove(x)
print(nums) # Output: [1, 3]

# Use list comprehension (recommended for filtering)
nums = [1, 2, 3, 4]
new_nums = [x for x in nums if x % 2 != 0]
print(new_nums) # Output: [1, 3]
```

### Q6. What does `list.sort()` return?
The `sort()` method sorts the list **in-place** and returns `None`. It does not return the sorted list itself.

```python
a = [3, 1, 2]
result = a.sort()
print(result) # Output: None
print(a)      # Output: [1, 2, 3] (The list 'a' is modified)
```
If you need a new sorted list without modifying the original, use the built-in `sorted()` function:
```python
a = [3, 1, 2]
new_sorted_list = sorted(a)
print(new_sorted_list) # Output: [1, 2, 3]
print(a)               # Output: [3, 1, 2] (Original 'a' is unchanged)
```

### Q7. Can you convert a float directly to a list?
❌ **No**. A `float` object is not iterable, so `list(6.46)` will raise a `TypeError`.
**Correct way:** Convert the float to a string first, then to a list of characters.
```python
x = 6.46
result = list(str(x))
print(result) # Output: ['6', '.', '4', '6']
```

---

## 🚀 Python List Tricks (Pro Level)

### 1. List Comprehensions
A concise way to create lists based on existing iterables.
```python
# Create a list of squares
squares = [x**2 for x in range(1, 6)] # [1, 4, 9, 16, 25]

# Filter even numbers
even_numbers = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0] # [2, 4]

# List comprehension with conditional expression (ternary operator)
transformed_list = [x if x % 2 == 0 else -x for x in range(5)] # [0, -1, 2, -3, 4]
```

### 2. Swapping Values
Python allows for easy swapping of values without a temporary variable.
```python
a = 10
b = 20
a, b = b, a
print(f"a: {a}, b: {b}") # Output: a: 20, b: 10
```

### 3. Flattening a Nested List
Combine elements from sublists into a single flat list.
```python
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list) # Output: [1, 2, 3, 4, 5, 6]
```

### 4. Chunking a List
Divide a list into smaller sublists of a specified size.
```python
my_list = [1, 2, 3, 4, 5, 6]
chunk_size = 3
chunks = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]
print(chunks) # Output: [[1, 2, 3], [4, 5, 6]]
```

### 5. `all()` and `any()` Functions
*   `all(iterable)`: Returns `True` if all elements of the iterable are true (or if the iterable is empty).
*   `any(iterable)`: Returns `True` if any element of the iterable is true. If the iterable is empty, returns `False`.

```python
print(all([1, True, 'hello'])) # True
print(all([1, 0, True]))       # False (because 0 is falsy)
print(any([0, False, '']))     # False (all are falsy)
print(any([0, False, 'hi']))   # True
```

### 6. `zip()` Function
Combine elements from multiple iterables into tuples.
```python
names = ['Alice', 'Bob']
ages = [25, 30]
zipped_data = list(zip(names, ages))
print(zipped_data) # Output: [('Alice', 25), ('Bob', 30)]
```

---

## Conclusion
Lists are a fundamental and powerful data structure in Python. Mastering their characteristics, methods, and advanced techniques is crucial for efficient and effective Python programming.
