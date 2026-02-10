# Type Casting in Python (Complete Guide)

Type casting (or Type Conversion) is the process of converting a literal or a variable from one data type to another. This is essential when handling user input, processing data from APIs, or performing mathematical operations on mixed types.

---

## 1. Fundamental Type Casting

### 🔹 Integer Casting (`int()`)
Converts a value into an integer.

*   **From Float**: Truncates the decimal part (does not round).
    ```python
    int(3.99)  # 3
    int(-2.5)  # -2
    ```
*   **From Boolean**:
    ```python
    int(True)  # 1
    int(False) # 0
    ```
*   **From String**:
    *   String must contain **only digits**.
    *   Optional `+` or `-` sign at the start is allowed.
    *   **No decimal points** allowed in the string.
    *   **No spaces** allowed inside the number.
    ```python
    int("10")    # 10
    int("-5")    # -5
    # int("3.5")   # ❌ ValueError (String contains '.')
    # int("10a")   # ❌ ValueError (Contains character)
    ```
    > **Trick**: To convert a string float like `"3.5"` to int, convert to float first: `int(float("3.5"))`.

### 🔹 Float Casting (`float()`)
Converts a value into a floating-point number.

*   **From Int**: Adds `.0`.
    ```python
    float(10)    # 10.0
    ```
*   **From String**: Can handle integers or decimal strings.
    ```python
    float("3.5") # 3.5
    float("10")  # 10.0
    ```

### 🔹 Boolean Casting (`bool()`)
Converts a value to `True` or `False`. This is based on **Truthiness**.

*   **Falsy Values (Result -> `False`)**:
    1.  Zero: `0`, `0.0`, `0j`
    2.  `None`
    3.  Empty Collections: `""` (Empty String), `[]`, `()`, `{}`, `set()`
*   **Truthy Values (Result -> `True`)**:
    *   Everything else (e.g., `1`, `-1`, `" "`, `[0]`, `{'a': 1}`).

```python
bool(0)      # False
bool("Hi")   # True
bool("False")# True (Non-empty string!)
bool({})     # False
```

### 🔹 Complex Casting (`complex()`)
*   `complex(real)` -> `real + 0j`
*   `complex(real, imag)` -> `real + imag*j`
*   `complex("3+4j")` -> `3+4j` (⚠️ No spaces allowed around `+` or `-` in string).

---

## 2. Collection Type Casting

### 🔹 String to List / Tuple / Set
Iterates over the string and treats each character as an element.

```python
s = "Python"

list(s)   # ['P', 'y', 't', 'h', 'o', 'n']
tuple(s)  # ('P', 'y', 't', 'h', 'o', 'n')
set(s)    # {'P', 'y', 't', 'h', 'o', 'n'} (Order is random)
# dict(s) # ❌ ValueError (Needs key-value pairs)
```

### 🔹 List / Tuple / Set Inter-conversion
*   `list()`: Preserves order, allows duplicates.
*   `tuple()`: Preserves order, immutable.
*   `set()`: **Removes duplicates**, destroys order.

```python
nums = [1, 2, 2, 3]
print(set(nums))  # {1, 2, 3} (Unique elements)
```

---

## 3. Dictionary Casting (`dict()`) - ⚠️ The Tricky Part

To convert something into a dictionary, the data must be a **sequence of Key-Value pairs**.

### ✅ Valid Structures
The input must be a collection (list/tuple) where **every item** is a collection of **exactly 2 elements** (Key, Value).

```python
# List of Lists
l = [[1, 'a'], [2, 'b']]
dict(l)  # {1: 'a', 2: 'b'}

# List of Tuples
l = [(1, 'a'), (2, 'b')]
dict(l)  # {1: 'a', 2: 'b'}

# Tuple of Strings (Length 2 strings)
# 'ab' splits into 'a' (Key) and 'b' (Value)
l = ('ab', 'xy')
dict(l)  # {'a': 'b', 'x': 'y'}
```

### ❌ Invalid Structures
```python
# dict(['abc'])
# ValueError: dictionary update sequence element has length 3; 2 is required
```

### 📌 Key Override Rule
If duplicate keys exist, the **last value** overrides the previous one.
```python
dict([('a', 1), ('a', 2)])
# {'a': 2}
```

---

## 4. Specific Type Conversions

### 🔹 Tuple Type Casting
```python
t1 = (2.3, 22, 2, 55, "RaviRaj", False)

# ✅ Tuple → List / Set / String
list(t1)
set(t1)
str(t1)

# ❌ Tuple → Dictionary
# dict(t1)   # ❌ TypeError: Tuple elements are not key–value pairs.
```

### 🔹 Set Type Casting
```python
s1 = {1, 2, 3, 4}

# ❌ Set → int / float
# int(s1)     # ❌ TypeError
# float(s1)   # ❌ TypeError

# ✅ Set → List / Tuple / String
list(s1)
tuple(s1)
str(s1)

# ❌ Set → Dictionary
# dict(s1)    # ❌ TypeError: Set contains single values, not key–value pairs.
```

### 🔹 Dictionary Type Casting
```python
d1 = {'a': 10, 'b': 20, 'c': 30}

# ✅ Dictionary → Boolean
bool(d1)    # True (Any non-empty dictionary is True)
bool({})    # False

# ✅ Dictionary → List / Tuple / Set
# By default, only **keys** are converted.
list(d1)      # ['a', 'b', 'c']
tuple(d1)     # ('a', 'b', 'c')
set(d1)       # {'a', 'b', 'c'}

# 🔹 Dictionary Values & Items
list(d1.values())   # [10, 20, 30]
list(d1.items())    # [('a', 10), ('b', 20), ('c', 30)]
```

---

## ⚠️ Common Interview Mistakes (VERY IMPORTANT)

| Mistake | Correction |
| :--- | :--- |
| **"Strings cannot be typecasted to int"** | Wrong. **Numeric** strings CAN be converted. |
| **Using `string()` function** | Wrong. The correct function is `str()`. |
| **Forgetting Dict requirements** | Dicts ALWAYS need key-value pair inputs (length 2). |
| **`bool()` validates logic** | Wrong. `bool()` only checks if a container is **empty** or **not**. |

---

## 🎯 VVI Interview Questions

### Q1. Can we convert "Python" into int?
❌ **No** — it is non-numeric.

### Q2. Why does `int(3.9)` return `3`?
✔ Decimal part is **truncated**, not rounded.

### Q3. Why does `dict(['abc'])` give an error?
✔ Length must be **exactly 2** for key–value pairs. `'abc'` has length 3.

### Q4. What does `bool({})` return?
✔ **False** — it is an empty dictionary.

### Q5. What happens if duplicate keys exist in conversion?
✔ The **last value** overrides the previous one. `dict([('a', 1), ('a', 2)])` -> `{'a': 2}`.
