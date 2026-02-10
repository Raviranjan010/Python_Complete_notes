# Relational (Comparison) Operators in Python

This guide explains the detailed logic behind how Python compares **Strings** and **Lists**, which often confuses beginners.

---

## 🔍 Comparison Operators (`>`, `<`, `==`)
Python compares sequences **lexicographically** (element by element), NOT just by length.

---

## 🧵 1. String Comparison Rules

### 🔹 Core Rules
1.  **Character by Character**: Comparison happens left to right.
2.  **ASCII/Unicode Values**: It treats characters as numbers (ASCII).
3.  **Stop Condition**: Comparison stops at the **first different** character.
4.  **Case Sensitivity**: Uppercase letters are "smaller" than lowercase letters.

### 📌 ASCII Reference (Important)
| Character | ASCII Value |
| :--- | :--- |
| 'A' | 65 |
| 'Z' | 90 |
| 'a' | 97 |
| 'z' | 122 |

> **Trick:** Capital letters come **before** (are smaller than) lowercase letters.

### ✅ Examples with Reasons

#### Example 1: ` 'Amaan' > 'Anshuman' `
*   **Result**: `False`
*   **Reason**:
    1.  `'A'` == `'A'` (Move to next)
    2.  `'m'` (109) vs `'n'` (110)
    3.  `109 < 110` -> False.

#### Example 2: ` 'Hello' > 'Python' `
*   **Result**: `False`
*   **Reason**: `'H'` (72) < `'P'` (80).

#### Example 3: ` 'Python' > 'hello' `
*   **Result**: `False`
*   **Reason**: `'P'` (80) < `'h'` (104). (Remember: Uppercase is smaller!)

---

## 📦 2. List Comparison Rules

### 🔹 Core Rules
1.  **Element by Element**: Compare index 0 vs index 0, then 1 vs 1, etc.
2.  **First Difference Decides**: The first unequal pair determines the result.
3.  **Equality**: Lists are equal only if ALL elements are equal.
4.  **Length**: Length DOES NOT matter unless one list is a "prefix" of the other (e.g., `[1,2]` < `[1,2,3]`).

### ✅ Examples with Reasons

#### Example 1: ` [10, 20, 30] > [1, 2, 3] `
*   **Result**: `True`
*   **Reason**: Index 0 compare: `10 > 1` is True. Stop.

#### Example 2: ` [10, 20, 30] > [1, 30, 40] `
*   **Result**: `True`
*   **Reason**: Index 0 compare: `10 > 1` is True. Stop.

#### Example 3: ` [10, 20, 30] > [10, 20, 30] `
*   **Result**: `False`
*   **Reason**: All elements are equal.

#### Example 4: ` [1, 20, 30] > [1, 20, 40] `
*   **Result**: `False`
*   **Reason**:
    1.  `1 == 1`
    2.  `20 == 20`
    3.  `30 < 40` -> False.

---

## 🧠 Summary Table (Cheat Sheet)

| Comparison Type | Rule |
| :--- | :--- |
| **String vs String** | Uses ASCII values ('A' < 'a'). |
| **List vs List** | Element-by-element left to right. |
| **Mixed Types** | `[1] > "A"` raises `TypeError`. |
| **Equal Sequences** | `>` and `<` always return `False`. |
