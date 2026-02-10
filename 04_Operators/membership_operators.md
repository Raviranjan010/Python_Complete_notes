# Membership Operators (`in`, `not in`)

Membership operators test whether a value is found within a sequence (string, list, tuple, set, or dictionary).

| Operator | Description | Example |
| :--- | :--- | :--- |
| `in` | Returns `True` if a value is found in the sequence. | `5 in [1, 2, 5]` -> `True` |
| `not in` | Returns `True` if a value is **not** found. | `10 not in [1, 2]` -> `True` |

---

## 🔍 Examples

### 1. Lists
```python
l = [10, 20, 30]

print(10 in l)      # True
print(1 in l)       # False (1 is not in list)
print(100 not in l) # True
```

### 2. Sets
```python
s = {10, 20, 30}

print(1 in s)    # False
print(1 not in s) # True
```

### 3. Strings
Checks if a substring exists.
```python
s = "Hello Python"
print('Python' in s) # True
print('z' in s)      # False
```

### 4. Dictionaries
Checks if a **Key** exists (not value).
```python
d = {'a': 1, 'b': 2}
print('a' in d)  # True
print(1 in d)    # False (Checks keys only)
```
