# Numeric Data Types

Python provides three distinct numeric types: **Integers**, **Floating Point Numbers**, and **Complex Numbers**.

## 1. Integers (`int`)
Integers are whole numbers, positive or negative, without decimals, of unlimited length.

```python
x = 10
y = -505
z = 999999999999 # Python handles arbitrarily large integers automatically

print(type(x)) # <class 'int'>
```

## 2. Floating Point Numbers (`float`)
Floats represent real numbers and are written with a decimal point dividing the integer and fractional parts. They can also be scientific numbers with an "e" to indicate the power of 10.

```python
x = 1.10
y = 1.0
z = -35.59
scientific = 35e3 # 35 * 10^3 = 35000.0

print(type(x)) # <class 'float'>
```

> [!NOTE]
> Floating point arithmetic can sometimes be imprecise due to binary representation (e.g., `0.1 + 0.2` might result in `0.30000000000000004`).

## 3. Complex Numbers (`complex`)
Complete numbers have a real part and an imaginary part. In Python, the imaginary part is written with a `j` suffix.

**Syntax**: `real + imaginary j`

```python
c = 3 + 5j
print(type(c)) # <class 'complex'>

# Attributes
print(c.real)  # 3.0
print(c.imag)  # 5.0
```

*   **Real Part**: `3` (stored as float)
*   **Imaginary Part**: `5` (stored as float)
*   **Unit**: Python uses `j` or `J`, not `i`.

### Operations on Complex Numbers
```python
a = 1 + 2j
b = 3 + 5j

# Addition
print(a + b) # (4+7j)

# Multiplication
print(a * b) # (-7+11j)
```

## 4. Boolean with Numbers
Booleans behave like integers in arithmetic.
*   `True` → `1`
*   `False` → `0`

```python
print(True + 1)   # Output: 2
print(False * 10) # Output: 0
```
**Point to Remember**: Booleans are a subclass of `int`.

## 🧠 Type Conversion (Casting)
You can convert between types using `int()`, `float()`, and `complex()`.

```python
x = 1    # int
y = 2.8  # float

# Convert int to float
a = float(x)  # 1.0

# Convert float to int
b = int(y)    # 2 (Note: it truncates, doesn't round!)
```

---

### 🧠 Interview Point: Integer Cache
**Q: What is Integer Caching (or Interning)?**
**A:** Python caches small integers (usually `-5` to `256`) as unique objects to save memory.
-   If `a = 5` and `b = 5`, they point to the exact same object in memory (`id(a) == id(b)` is True).
-   If `a = 1000` and `b = 1000`, they *might* be different objects (though recent Python versions optimize this too in some contexts).
