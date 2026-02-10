# 📘 Master Pattern Printing in Python

## 🔑 ONE CORE TRICK (Never Forget This)
> **Every pattern = 2 loops + 1 decision**

*   **Outer loop**  → Rows (`i`)
*   **Inner loop**  → Columns (`j`)
*   **Print logic** → What to print

> **Tip:** If you know what changes row-by-row, the pattern is solved.

---

## 🧪 Universal Python Template

```python
n = 4

for i in range(n):          # Rows
    for j in range(n):      # Columns
        print("*", end=" ")
    print()                 # New line after each row
```

### 📌 Golden Python Rule
*   `end=" "` → Prints on the **same line**.
*   `print()` → Moves to a **new line**.

---

## 🧠 GOLDEN MEMORY TRICKS (EXAM HACK)

| Pattern Type | Inner Loop | Memory Trick |
| :--- | :--- | :--- |
| **Square** | `range(n)` | Fixed × Fixed |
| **Increasing** | `range(i+1)` | Row grows |
| **Decreasing** | `range(n-i)` | Row shrinks |
| **Right aligned** | spaces first | Mirror = space first |
| **Hollow** | `if` border | Boundary only |
| **Diagonal** | `i == j` | Row = Column |
| **Reverse diagonal** | `i + j == n-1` | Opposite corner |

---

## 1️⃣ Square Patterns (Python)

### Pattern 1: Row Numbers
**Logic:** Output depends on the row number (`i`).

```python
n = 4
for i in range(n):
    for j in range(n):
        print(i+1, end=" ")
    print()
```
**Output:**
```
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

### Pattern 2: Row Number with Symbol
```python
n = 4
for i in range(n):
    for j in range(n):
        print(str(i+1) + "*", end="")
    print()
```

### Pattern 3: Column Numbers
**Logic:** Output changes left → right (`j`).

```python
n = 4
for i in range(n):
    for j in range(n):
        print(j, end=" ")
    print()
```
**Output:**
```
0 1 2 3
0 1 2 3
0 1 2 3
0 1 2 3
```

### Pattern 4: Star Square
```python
n = 4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
```

---

## 2️⃣ Increasing Triangle (Most Important)

> **🔑 Shortcut:** Columns = row number (`range(i+1)`)

### Pattern 5: Star Triangle
```python
n = 4
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
```
**Output:**
```
*
* *
* * *
* * * *
```

### Pattern 6: Number Triangle (Row-based)
```python
n = 4
for i in range(n):
    for j in range(i+1):
        print(i+1, end=" ")
    print()
```

### Pattern 7: Number Triangle (Column-based)
```python
n = 4
for i in range(n):
    for j in range(i+1):
        print(j, end=" ")
    print()
```

### Pattern 11: Continuous Characters
**Logic:** Use a single variable outside the loop.

```python
ch = ord('A')

for i in range(1, 4):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
```
**Output:**
```
A
B C
D E F
```

---

## 3️⃣ Decreasing Triangle

> **🔑 Shortcut:** Columns = `n - i`

### Pattern 8: Inverted Star Triangle
```python
n = 4
for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()
```

### Pattern 9: Inverted Column Numbers
```python
n = 4
for i in range(n):
    for j in range(n - i):
        print(j, end=" ")
    print()
```

### Pattern 10: Inverted Row Numbers
```python
n = 4
for i in range(n):
    for j in range(n - i):
        print(i, end=" ")
    print()
```

---

## 4️⃣ Conditional Patterns (VERY IMPORTANT)

### Pattern 12: Continuous Character Square
```python
ch = ord('A')
n = 3

for i in range(n):
    for j in range(n):
        print(chr(ch), end=" ")
        ch += 1
    print()
```

### Pattern 13: Hollow Square
**Boundary Formula:** `i == 0` or `i == n-1` or `j == 0` or `j == n-1`

```python
n = 4
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

### Pattern 14: Diagonal
**Mantra:** Diagonal → row equals column (`i == j`)

```python
n = 4
for i in range(n):
    for j in range(n):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

### Pattern 15: Reverse Diagonal
**Mantra:** Reverse Diagonal → `i + j == n - 1`

```python
n = 4
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

---

## 5️⃣ Mirrored / Space Patterns

> **🔑 Rule:** Spaces first → Stars later

### Pattern 16: Right Aligned Triangle
```python
n = 4
for i in range(1, n+1):
    print("  " * (n-i), end="")
    print("* " * i)
```

### Pattern 18: Inverted Right Triangle
```python
n = 4
for i in range(n):
    print("  " * i, end="")
    print("* " * (n-i))
```

---

## 6️⃣ Pyramid & Diamond (High Level)

### Pattern 19: Pyramid
```python
n = 4
for i in range(1, n+1):
    print("  " * (n-i), end="")
    for j in range(i):
        print("*", end="   ")
    print()
```

### Pattern 20: Inverted Pyramid
```python
n = 4
for i in range(n):
    print("  " * i, end="")
    for j in range(n-i):
        print("*", end="   ")
    print()
```

### Pattern 21: Diamond
**Formula:** Pyramid + Reverse Pyramid

```python
n = 4

# Top
for i in range(1, n+1):
    print("  " * (n-i), end="")
    for j in range(i):
        print("*", end="   ")
    print()

# Bottom
for i in range(n-1, 0, -1):
    print("  " * (n-i), end="")
    for j in range(i):
        print("*", end="   ")
    print()
```

---

## 🏆 FINAL MEMORY CHEAT CODE (WRITE THIS IN EXAM)

| Pattern | Logic / Range |
| :--- | :--- |
| **Square** | `range(n)` |
| **Increase** | `range(i+1)` |
| **Decrease** | `range(n-i)` |
| **Right Align** | spaces = `n-i` |
| **Hollow** | boundary condition |
| **Diagonal** | `i == j` |
| **Reverse Diag** | `i + j == n-1` |
