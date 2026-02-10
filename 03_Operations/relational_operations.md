# Comparison (Relational) Operators

Comparison operators compare two values and return a Boolean result (`True` or `False`).

| Operator | Meaning |
| :--- | :--- |
| `>` | Greater Than |
| `<` | Less Than |
| `==` | Equal To |
| `!=` | Not Equal To |
| `>=` | Greater or Equal |
| `<=` | Less or Equal |

---

## 1. Comparing Numbers
Standard math comparison.
```python
10 > 5   # True
10 == 10 # True
```

---

## 2. Comparing Strings
Strings are compared **character by character** using their **ASCII/Unicode** values.

*   `'a'` (97) > `'A'` (65) -> **True**
*   Comparison stops at the first different character.

```python
'Python' > 'Hello'
# 'P' (80) vs 'H' (72) -> 80 > 72 -> True

'apple' > 'banana'
# 'a' (97) vs 'b' (98) -> 97 > 98 -> False

# Case Sensitivity
'Amaan' > 'Anshuman' # False ('A'=='A', 'm'(109) < 'n'(110))
'A' > 'a'            # False (65 < 97)
```

---

## 3. Comparing Lists
Lists are compared **element by element** from left to right.

1.  Compare `list1[0]` with `list2[0]`.
2.  If equal, move to index 1.
3.  If not equal, the list with the larger element is considered "greater".
4.  Total length only matters if one list is a prefix of the other.

```python
[10, 20, 30] > [1, 2, 3]   # True (10 > 1)
[10, 20, 30] > [1, 30, 40] # True (10 > 1)
[10, 20, 30] > [10, 20, 30]# False (Equal)

# Tricky Case
[1, 20, 30] > [1, 20, 40]  # False (30 < 40)
```

### Type Comparability
> [!WARNING]
> Lists cannot be compared with other types like `int` or `set`.
> `[3] > {3}` -> **TypeError**
> `22 > [22]` -> **TypeError**

---

## 4. Comparing Sets
For sets, relational operators check for **Subset/Superset** relationships, not element value magnitude.

*   `A > B`: Is A a **proper superset** of B? (A contains all of B, plus more).
*   `A < B`: Is A a **proper subset** of B?
*   `A >= B`: Is A a superset of B?
*   `A <= B`: Is A a subset of B?

```python
{1, 2, 3} > {1, 2}      # True (Superset)
{1, 2, 3} > {1, 5}      # False (5 is not in first set)
{1, 2} < {1, 2, 3, 4}   # True (Subset)
```

---

## 5. Equality (`==`)
Checks if values are equal.
*   `1 == 1.0` -> **True** (Value is same).
*   `10 == (10)` -> **True**.
*   `10 == (10,)` -> **False** (Int vs Tuple).
*   `[10] != 10.0` -> **True** (List vs Float are different types).
*   `10 != 10.0` -> **False** (Values are equal).

---

## 🎯 VVI Interview Questions

### Q1. What is the difference between `==` and `is`?
*   `==` checks **Value Equality** (Do they have the same content?).
*   `is` checks **Identity / Memory Address** (Are they the exact same object?).

### Q2. `10 > '2'`?
❌ **TypeError**. Python 3 does not support comparison between `int` and `str`.

### Q3. `[10] == (10,)`?
❌ **False**. Lists and Tuples are different types, so they are not equal even if contents look similar.
