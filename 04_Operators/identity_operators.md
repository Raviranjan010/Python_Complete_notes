# Identity Operators (`is`, `is not`)

Identity operators compare the **memory location** (address) of two objects, not just their values.

| Operator | Description | Example |
| :--- | :--- | :--- |
| `is` | Returns `True` if both variables point to the **same object**. | `x is y` |
| `is not` | Returns `True` if variables point to **different objects**. | `x is not y` |

---

## 🔍 `is` vs `==`

*   `==`: **Value Comparison**. Checks if values are equal.
*   `is`: **Reference Comparison**. Checks if they are the exact same object in memory.

```python
a = 10
b = 10
print(a is b)  # True (Python caches small integers, so they point to same address)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2) # True (Values are same)
print(l1 is l2) # False (Different list objects in memory)
```

## 🧠 Lab Example
```python
a = 10
b = 20
c = 10

print(a is c)     # True  (Both point to 10)
print(a is b)     # False
print(a is not b) # True
```

> **Note**: For immutable types (int, str, tuple), Python often reuses objects (Interning). For mutable types (list, set, dict), new objects are always created.
