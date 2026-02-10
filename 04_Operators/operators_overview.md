# Python Operators Overview

Operators are special symbols that perform operations on variables and values.

## Types of Operators
1.  **Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
2.  **Comparison (Relational)**: `==`, `!=`, `>`, `<`, `>=`, `<=`
3.  **Logical**: `and`, `or`, `not`
4.  **Bitwise**: `&`, `|`, `^`, `~`, `<<`, `>>`
5.  **Assignment**: `=`, `+=`, `-=`, etc.
6.  **Identity**: `is`, `is not`
7.  **Membership**: `in`, `not in`

---

## ⚠️ Operator Traps & Tricks (Must Read)

### 1. Equality vs Identity
*   `10 == 10.0` is **True** (Values are equal).
*   `[10] == (10,)` is **False** (Different types: List vs Tuple).
*   `a = [1]; b = [1]; a is b` is **False** (Different objects).
*   `a = 10; b = 10; a is b` is **True** (Small integer caching).

### 2. Logical Short-Circuiting
*   **`and`**: Returns the **first Falsy** value. If all are True, returns the **last** value.
    *   `10 and 0` -> `0`
    *   `10 and 20` -> `20`
*   **`or`**: Returns the **first Truthy** value. If all are False, returns the **last** value.
    *   `10 or 20` -> `10`
    *   `0 or []` -> `[]`

### 3. Relational Chaining
*   `1 < 2 < 3` is equivalent to `1 < 2 and 2 < 3` -> **True**.
*   `10 > 5 > 20` is `10 > 5 and 5 > 20` -> **False**.

### 4. Floating Point Arithmetic
*   `0.1 + 0.2 == 0.3` is **False** due to floating-point precision issues.
