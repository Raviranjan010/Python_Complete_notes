# Logical Operators

Logical operators are used to combine conditional statements.

| Operator | Description |
| :--- | :--- |
| `and` | Returns `True` if **both** statements are true. |
| `or` | Returns `True` if **at least one** statement is true. |
| `not` | Reverses the result, returns `False` if the result is true. |

---

## 1. Short-Circuit Evaluation

Python uses short-circuit logic for non-boolean values. Implicitly, `0`, `False`, `None`, `[]`, `""` are treated as **False**. All other values are **True**.

### The `and` Rule
*   If the first operand is **False**, Python stops and returns the **first operand**.
*   If the first operand is **True**, Python checks and returns the **second operand**.

```python
10 and 20   # 20 (10 is True, return 2nd)
0 and 20    # 0  (0 is False, return 1st)
[] and 10   # [] (Empty list is False, return 1st)
```

### The `or` Rule
*   If the first operand is **True**, Python stops and returns the **first operand**.
*   If the first operand is **False**, Python checks and returns the **second operand**.

```python
10 or 20    # 10 (10 is True, return 1st)
0 or 20     # 20 (0 is False, return 2nd)
```

---

## 2. Examples

```python
not(True)   # False
not(0)      # True

# Complex Expression
# True and False -> False
# not(False) -> True
result = not(10 > 2 and 5 < 1)
print(result) # True
```

### 3. Tricky Short-Circuit Examples
```python
# and: Returns first Falsy, else last value
10 and 0       # 0
0 and 'hi'     # 0
'Hello' and 'Hi' # 'Hi'
{} and 0.0     # {}

# or: Returns first Truthy, else last value
10 or 0        # 10
0 or 'hi'      # 'hi'
{} or []       # [] (Both false, returns last)
```

### 4. Logic Truth Table Cheat Sheet
| A | B | `A and B` | `A or B` |
| :--- | :--- | :--- | :--- |
| **True** | **True** | True | True |
| **True** | **False** | False | True |
| **False** | **True** | False | True |
| **False** | **False** | False | False |

> **Precedence Rule**: `not` > `and` > `or`.
> `{} and not("") or []` -> `{} or []` -> `[]`
