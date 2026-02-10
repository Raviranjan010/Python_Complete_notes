# Slicing in Python

Picking a part of any data type is called **slicing**. We can do slicing in strings, lists, and tuples.

**Syntax**:
```python
var_name[starting_index : ending_index : step]
```

---

## 1. List Slicing
Slicing allows you to extract sub-parts of a list.

```python
a = [10, 20, 30, 40, 50]

# Positive Slicing: [start : end]
# Start is inclusive, End is exclusive.
print(a[1:4])  # [20, 30, 40]

# Negative Slicing
# Indices: -5(10), -4(20), -3(30), -2(40), -1(50)
print(a[-4:-1])  # [20, 30, 40]
```

---

## 2. String Slicing
Strings can be sliced similarly to lists.

```python
s = 'Dictionary'

# Full string
print(s[::1])  # 'Dictionary'

# Reverse string
print(s[::-1])  # 'yranoitciD'

# Substring
print(s[0:5])  # 'Dicti'
```

---

## 3. Tricky Negative Slicing (The "Empty String" Trap)
A common mistake is trying to slice backwards with a positive step.

*   `s[-1:-4]` returns an **empty string** because the default step is `+1` (Left -> Right). You cannot go from index `-1` (Right) to `-4` (Left) moving rightwards.

**To go backwards, you MUST specify a negative step.**

```python
s = 'Dictionary'

# Wrong
print(s[-1:-4])   # '' (Empty)

# Correct
print(s[-1:-4:-1]) # 'yra'
print(s[-4:-1])    # 'nar' (Standard left-to-right using negative indices)

# Advanced Backwards Step
# Start -1, End -10, Step -2 (Skip every 2nd char backwards)
print(s[-1:-10:-2]) # 'yaoti'
```

---

## 4. Nested Slicing (Deep Access)
You can slice elements inside other elements (Nested Lists/Tuples/Dictionaries).

```python
s3 = ['Hello class', (5.2+2.36j, 11, False), {'a': 101, 10.1: 5500}]

# Fetch reverse of the tuple at index 1
# s3[1] is the tuple: (5.2+2.36j, 11, False)
# [::-1] reverses it.
rev = s3[1][::-1]
print(rev) # (False, 11, (5.2+2.36j))
```

### Complex Nested Structure Example
```python
s7 = {'a': ["This is a list"], 'b': [10, 20, 30, ("Hello", 'Guys')]}

# Goal: Fetch reverse of 'Guys'
# Path:
# 1. s7['b']       -> [10, 20, 30, ("Hello", 'Guys')]
# 2. [3]           -> ("Hello", 'Guys')
# 3. [1]           -> 'Guys'
# 4. [::-1]        -> 'syuG'

print(s7['b'][3][1][::-1]) # 'syuG'
```

---

## 5. List Inside List Example
```python
l6 = [1, 2.2, [2+2j, True, ['Yadav ji', 'Pandey Ji', False]]]

# Access 'Pandey Ji'
# l6[2] -> Inner list
# [2]   -> Innermost list
# [1]   -> 'Pandey Ji'

print(l6[2][2][1])   # 'Pandey Ji'
```
