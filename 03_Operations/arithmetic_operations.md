# Arithmetic Operators

Standard mathematical operations.

| Operator | Name | Example | Result |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `10 + 20` | `30` |
| `-` | Subtraction | `10 - 2` | `8` |
| `*` | Multiplication | `10 * 2` | `20` |
| `/` | Division | `10 / 2` | `5.0` (Always float) |
| `//` | Floor Div | `10 // 3` | `3` (Integer part) |
| `%` | Modulus | `10 % 3` | `1` (Remainder) |
| `**` | Exponent | `2 ** 3` | `8` ($2^3$) |

---

## Behavior with Different Data Types

### 1. Addition (`+`)
*   **Numbers**: Adds values. `10 + 20` -> `30`
*   **Strings**: Concatenation. `'Hi' + 'Bye'` -> `'HiBye'`
*   **Lists**: Merging. `[1, 2] + [3, 4]` -> `[1, 2, 3, 4]`
*   **Tuples**: Merging. `(1, 2) + (3, 4)` -> `(1, 2, 3, 4)`

> [!WARNING]
> **Type Errors**:
> You cannot add different types directly (e.g., `list + tuple`).
> `[1, 2] + (3, 4)` -> **TypeError**

### 2. Multiplication (`*`)
*   **Numbers**: Multiplies. `10 * 2` -> `20`
*   **Strings**: Repetition. `'Hi' * 3` -> `'HiHiHi'`
*   **Lists**: Repetition. `[1] * 3` -> `[1, 1, 1]`

### 3. Subtraction (`-`)
*   **Sets**: Difference operation.
    ```python
    {1, 2, 3} - {2} # {1, 3} (Removes common elements)
    ```
*   **Note**: Subtraction is **not** supported for Strings or Lists.

---

## 🔍 Operator Support by Data Type

| Operator | int | float | bool | complex | list | tuple | set | dict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **+** | ✅ | ✅ | ✅ | ✅ | ✅ (Concat) | ✅ (Concat) | ❌ | ❌ |
| **-** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ (Diff) | ❌ |
| **\*** | ✅ | ✅ | ✅ | ✅ | ✅ (Repeat) | ✅ (Repeat) | ❌ | ❌ |
| **/** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **//** | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **%** | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **\*\*** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |

---

## 🧠 Advanced Concepts

### 1. Complex Number Power
The code `(1 + 2j) ** 2` expands algebraically:
$(1 + 2j)^2 = 1^2 + 2(1)(2j) + (2j)^2$
$= 1 + 4j + 4j^2$
Since $j^2 = -1$:
$= 1 + 4j - 4$
$= -3 + 4j$

### 2. Concatenation Support
| Type | Example | Result |
| :--- | :--- | :--- |
| **String** | `"A" + "B"` | `"AB"` |
| **List** | `[1] + [2]` | `[1, 2]` |
| **Tuple** | `(1,) + (2,)` | `(1, 2)` |

> **Trap**: `10 + "20"` raises `TypeError`. Concatenation works only with the **same** sequence type.

---

## 🎯 VVI Interview Questions

### Q1. What is the result of `10 // 3` vs `10 / 3`?
*   `10 // 3` = `3` (Integer floor division)
*   `10 / 3` = `3.333...` (Float division)

### Q2. Can you add two sets using `+`?
❌ **No**. Sets do not support `+`. You must use `.union()` or `|`.

### Q3. What is the result of `True + True`?
✅ `2`. Because `True` acts as `1` in arithmetic operations.

### Q4. What happens if you multiply a list by a negative number?
✅ You get an empty list `[]`. `[1, 2] * -1` -> `[]`.

### Q5. Explain `(10 + 5j) / 5`.
✅ `(2 + 1j)`. The division applies to both real and imaginary parts.
