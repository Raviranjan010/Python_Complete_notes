# Python Loops (`while` & `for`)

Loops allow you to execute a block of code repeatedly.

---

## 1. `while` Loop Programs

### Basic Number Series
```python
# Print 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
```

### Series: 10, 20, 30 ... 300
```python
i = 10
while i <= 300:
    print(i, end=" ")
    i += 10
```

### Reverse Series: 105, 98 ... 7
```python
i = 105
while i >= 7:
    print(i, end=" ")
    i -= 7
```

### Sum of First 10 Natural Numbers
```python
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("Sum =", total)
```

---

## 2. `for` Loop Programs

### Iterating Over a String
```python
s = "powerbi"
for char in s:
    print(char, end=" ")
```

### Multiplication Table
```python
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
```

### Find Length without `len()`
```python
s = "Python"
count = 0
for i in s:
    count += 1
print("Length:", count)
```

### Count Vowels
```python
s = "Education"
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Vowel Count:", count)
```

---

## 3. String Manipulation with Loops

### Reverse String
```python
# Using Loop
s = "python"
rev = ""
for char in s:
    rev = char + rev
print(rev) 

# Shortcut
print(s[::-1])
```

### Replace Space with Underscore
```python
s = "This is Python"
res = ""
for char in s:
    if char == " ":
        res += "_"
    else:
        res += char
print(res)
```

---

## 4. List Operations with Loops

### Remove Duplicates (Preserving Order)
```python
items = [10, 20, 10, 30, 20]
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
print(unique)
```

### Extract Vowels from Mixed List
```python
data = [10, 'Hello', 5.5, 'World']
vowels = "aeiouAEIOU"
extracted = []

for item in data:
    # Convert element to string to iterate chars
    for char in str(item):
        if char in vowels:
            extracted.append(char)
print(extracted)
```

---

## 5. Loop Control Keywords

| Keyword | Use |
| :--- | :--- |
| `break` | Stops the loop immediately. |
| `continue` | Skips the current iteration and jumps to the next. |
| `pass` | Null statement, does nothing (placeholder). |

### Prime Number Check (Using `break`)
```python
n = 13
is_prime = True
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime")
else:
    print("Not Prime")
```

---

## 🧠 Logic Breakdown (Exam Favorites)

### 1. Reverse a Number Logic
*   **Concept**: Extract last digit -> Add to result -> Remove last digit.
*   **Formula**: `rev = rev * 10 + last_digit`
```python
n = 123
rev = 0
while n > 0:
    last = n % 10
    rev = rev * 10 + last
    n = n // 10
```

### 2. Series Logic
*   **Increments**: `i += step` (e.g., 10, 20, 30...)
*   **Decrements**: `i -= step` (e.g., 100, 95, 90...)
*   **Squares**: `print(i * i)` inside the loop.

### 3. Loop `else` Block
*   A `for` or `while` loop can have an `else` block.
*   It executes **only if the loop completes normally** (i.e., NO `break` was encountered).
```python
for i in range(5):
    if i == 10: break
else:
    print("Loop finished successfully!")
```

### 4. Trap: Modifying List While Iterating
**Never start removing items from a list while iterating over it with a `for` loop.**

#### The Problem
```python
nums = [10, 20, 30, 40, 50]
for n in nums:
    if n > 20:
        nums.remove(n) 
# Result: [10, 20, 40] (30 was skipped!)
```
**Reason**: When you remove an item, the indices shift. The loop moves to the next index, skipping the element that shifted into the current spot.

#### The Fix
Iterate over a **copy** of the list.
```python
nums = [10, 20, 30, 40, 50]
for n in nums[:]: # [:] creates a copy
    if n > 20:
        nums.remove(n)
# Result: [10, 20] (Correct!)
```
