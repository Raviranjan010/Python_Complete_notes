# 📖 Dictionaries in Python (`dict`)

A **Dictionary** is a mutable, ordered (since Python 3.7) collection of **Key-Value** pairs. Each key must be unique and immutable.

**Syntax**: `{key: value, key2: value2}`

```python
d = {
    "language": "Python",
    "version": 3.11,
    1: "an integer key"
}
```

---

## 1. Key Characteristics
*   **Unordered**: (Historically). From Python 3.7+, insertion order is preserved, but you should access by Key, not index.
*   **Mutable**: Values can be changed.
*   **Keys**: Must be **Immutable** and **Hashable** (int, float, str, tuple). You cannot use a list or another dictionary as a key.
*   **Values**: Can be anything (mutable or immutable).

> [!NOTE]
> Dictionaries **cannot be compared** using relational operators (`>`, `<`, `>=`, `<=`). Attempting to do so will result in a `TypeError`. However, they can be compared for equality (`==`) and inequality (`!=`) based on their key-value pairs.


---

## 2. Accessing Elements
Dictionaries do not use numeric indexing (0, 1, 2). They use **Keys**.

```python
d = {1: 'A', 'b': 'Ball'}

print(d[1])   # Output: 'A'
print(d['b']) # Output: 'Ball'

# ❌ Error
# print(d[0]) # KeyError (unless 0 is a key)
```

---

## 3. Nested Dictionaries & Complex Access
*From Lab Logs*

```python
d4 = {
    1: 10,
    'a': {2.2, 10, (20+2j)},  # Set inside Dict
    'b': ['Hi', 10]           # List inside Dict
}

# Fetch 'Hi'
print(d4['b'][0])  # 'Hi'

# Fetch Reverse of 'Hi'
print(d4['b'][0][::-1]) # 'iH'
```

---

## 4. Common Methods

| Method | Description |
| :--- | :--- |
| `d.keys()` | Returns list of keys. |
| `d.values()` | Returns list of values. |
| `d.items()` | Returns list of (key, value) tuples. |
| `d.get(key)` | Returns value. Returns `None` if key not found (Safe). |
| `d.pop(key)` | Removes key and returns value. |

---

## 🎯 VVI Interview Questions & Tricks

### Q1. What happens if we define duplicate keys?
The **last** assignment wins. The previous value associated with that key is overwritten.
```python
d = {'a': 1, 'a': 2}
print(d) # {'a': 2}
```

### Q2. Can we use a List as a Dictionary Key?
**No**. Lists are mutable and unhashable, which means their hash value can change, making them unsuitable as dictionary keys. Dictionary keys must be immutable (and thus hashable).
```python
d = {[1,2]: "Value"} # ❌ TypeError: unhashable type: 'list'
```

### Q3. How to merge two dictionaries?
**Trick:** Use the `|` operator (Python 3.9+) or the `update()` method.
```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = d1 | d2  # {'a': 1, 'b': 2, 'c': 3, 'd': 4} (Python 3.9+)

d1.update(d2) # d1 becomes {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### Q4. How to safely access a dictionary value without risking a `KeyError`?
**Trick:** Use the `get()` method. It returns `None` (or a specified default value) if the key is not found, instead of raising an error.
```python
person = {"name": "Alice"}
print(person.get("name"))    # Alice
print(person.get("age"))     # None
print(person.get("age", 30)) # 30 (default value if key not found)
```

---

## 🔬 Lab Analysis: Dictionary Behavior

```python
# 1. Dictionary Creation & Key Overriding
# If a key is used more than once, the last value overrides the previous ones.
# Note: True and 1 are considered the same key (True == 1).
d2 = {True: 33, 2: False}
print(f"d2: {d2}")  
# Output: {True: 33, 2: False}

d3 = {1: 33, "a": "Acsa", 5: 43}
print(f"d3: {d3}")
print(f"Type of d3: {type(d3)}")

# 2. Accessing Elements
print(f"Value of 'a': {d3['a']}")  # 'Acsa'
print(f"Value of 5: {d3[5]}")      # 43

# Accessing a non-existent key raises KeyError
try:
    print(d3[3])
except KeyError as e:
    print(f"Error accessing d3[3]: {e}")

# 3. Nested Indexing
# Accessing characters inside a string value
# d3['a'] is 'Acsa'
print(f"2nd index of d3['a']: {d3['a'][2]}")  # 's'
print(f"3rd index of d3['a']: {d3['a'][3]}")  # 'a'

# 4. Complex Nested Dictionary
# Note on Tuples: (10) is an int, (10,) is a tuple.
d4 = {
    1: 10, 
    2: 2.25, 
    2.2: 3+22j, 
    4: False, 
    'a': {2.2, 10, (20+2j)},  # Set (unordered)
    'b': ['Hi', 10]           # List (ordered)
}

# Fetching 'Hi' from list inside dictionary
a1 = d4['b']
print(f"First element of d4['b']: {a1[0]}")  # 'Hi'

# Fetching False
print(f"Value at key 4: {d4[4]}")  # False

# Fetching 2.2 from the set at d4['a']
# Sets are unordered and do not support indexing.
# We cannot use d4['a'][0]. We must iterate or check membership.
print(f"Set at d4['a']: {d4['a']}")

# 5. Modifying Dictionaries
d = {1: 'Das', 2: 4}
d[1] = "Alia"    # Update existing key
d[7] = 'Thala'   # Add new key
print(f"Modified d: {d}")

# Removing elements using pop()
removed_value = d.pop(1)
print(f"Popped value: {removed_value}")
print(f"d after pop: {d}")
```
