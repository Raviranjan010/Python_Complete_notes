# String Data Type (`str`)
A **String** in Python is an **immutable sequence of characters**, primarily used for representing text. Once a string is created, its content cannot be changed. Any operation that appears to modify a string actually results in the creation of a new string object.

---

## 1. Key Characteristics
*   **Ordered**: Characters maintain their position, allowing access by index.
*   **Immutable**: Cannot be changed after creation. Operations that "modify" a string return a new string.
*   **Heterogeneous**: Can contain any Unicode character (letters, numbers, symbols).
*   **Allows Duplicates**: `s = "hello"` is a valid string.
*   **Indexed**: Supports 0-based positive indexing and -1-based negative indexing.
*   **Slicing**: Allows extraction of substrings.

---

## 2. String Creation
Strings can be defined using single, double, or triple quotes. Triple quotes are useful for multi-line strings.

```python
s1 = 'Hello'
s2 = "World"
s3 = """This is a
multi-line string."""
s4 = "Python"
```

---

## 3. String Indexing
Accessing individual characters using their position (index).

*   **Positive Indexing**: Starts from `0` for the first character (Left to Right).
*   **Negative Indexing**: Starts from `-1` for the last character (Right to Left).

```python
s = "PYTHON"

# Visualizing Indices:
#  P   Y   T   H   O   N
#  0   1   2   3   4   5  (Positive Indices)
# -6  -5  -4  -3  -2  -1  (Negative Indices)

print(s[0])    # Output: 'P'
print(s[-1])   # Output: 'N' (Last character)
print(s[3])    # Output: 'H'
print(s[-4])   # Output: 'T'
```

---

## 4. String Slicing
Slicing allows you to extract a portion (substring) of a string by specifying a range of indices.

**Syntax**: `string[start : end : step]`
*   `start`: The starting index (inclusive). If omitted, defaults to `0`.
*   `end`: The ending index (exclusive). If omitted, defaults to the length of the string.
*   `step`: The increment between indices. If omitted, defaults to `1`.

### Basic Slicing Rules
1.  **Positive Step (`step > 0`)**: Slices from Left to Right. The `end` index must be logically after the `start` index.
2.  **Negative Step (`step < 0`)**: Slices from Right to Left (reverses the order). The `start` index must be logically after the `end` index.
3.  **End is Exclusive**: Python stops *before* including the character at the `end` index.

### Examples
```python
s = "Dictionary"
# Indices: D=0, i=1, c=2, t=3, i=4, o=5, n=6, a=7, r=8, y=9

# Positive Slicing
print(s[0:5])      # Output: 'Dicti' (characters at indices 0, 1, 2, 3, 4)
print(s[3:])       # Output: 'tionary' (from index 3 to the end)
print(s[:6])       # Output: 'Dictio' (from beginning up to index 5)
print(s[::1])      # Output: 'Dictionary' (full string, step 1)
print(s[::2])      # Output: 'Dctoa' (every second character)

# Negative Slicing (Reverse)
print(s[::-1])     # Output: 'yranoitciD' (reverses the entire string)

# Slicing with negative indices and negative step
print(s[-1:-4:-1]) # Output: 'yra' (starts at 'y' (index -1), goes towards 'n' (index -4), step -1)

# Common Mistake: Slicing right-to-left with a positive step
print(s[-1:-4])    # Output: '' (Empty string, because default step is +1, which cannot go from -1 to -4)

# Advanced Example with negative step
s2 = 'Programming'
print(s2[-1:-12:-2]) # Output: 'gimroP'
# Explanation: Starts at 'g' (-1), goes towards 'P' (-12), taking every second character in reverse.
# Characters: g(-1), m(-3), o(-5), r(-7), g(-9), P(-11)
```

---

## 5. String Immutability (Important Concept)
Strings are immutable. This means you cannot change individual characters within a string after it has been created.

```python
my_string = "hello"
# my_string[0] = 'H' # This will raise a TypeError: 'str' object does not support item assignment

# Correct way to "modify" a string (by creating a new one):
new_string = 'H' + my_string[1:]
print(new_string) # Output: 'Hello'
```

---

## 6. Common String Methods
String methods return new strings; they do not modify the original string due to immutability.

### Case Conversion Methods
| Method | Description | Example |
| :--- | :--- | :--- |
| `s.upper()` | Converts all characters to uppercase. | `'hello'.upper()` -> `'HELLO'` |
| `s.lower()` | Converts all characters to lowercase. | `'HELLO'.lower()` -> `'hello'` |
| `s.title()` | Converts the first character of each word to uppercase. | `'hello world'.title()` -> `'Hello World'` |
| `s.capitalize()` | Converts the first character of the string to uppercase, others to lowercase. | `'hello world'.capitalize()` -> `'Hello world'` |
| `s.swapcase()` | Swaps case of all characters (upper to lower, lower to upper). | `'Hello World'.swapcase()` -> `'hELLO wORLD'` |

### Check Methods (Return `True` or `False`)
| Method | Description | Example |
| :--- | :--- | :--- |
| `s.isupper()` | Returns `True` if all cased characters are uppercase. | `'HELLO'.isupper()` -> `True` |
| `s.islower()` | Returns `True` if all cased characters are lowercase. | `'hello'.islower()` -> `True` |
| `s.isdigit()` | Returns `True` if all characters are digits and there is at least one character. | `'123'.isdigit()` -> `True` |
| `s.isalpha()` | Returns `True` if all characters are alphabetic and there is at least one character. | `'Python'.isalpha()` -> `True` |
| `s.isalnum()` | Returns `True` if all characters are alphanumeric (letters or numbers). | `'Py3'.isalnum()` -> `True` |
| `s.isspace()` | Returns `True` if all characters are whitespace and there is at least one character. | `'   '.isspace()` -> `True` |
| `s.startswith(prefix)` | Returns `True` if the string starts with the specified `prefix`. | `'Python'.startswith('Py')` -> `True` |
| `s.endswith(suffix)` | Returns `True` if the string ends with the specified `suffix`. | `'Python'.endswith('on')` -> `True` |

### Whitespace Removal Methods
| Method | Description | Example |
| :--- | :--- | :--- |
| `s.strip()` | Removes leading and trailing whitespace. | `'  hello  '.strip()` -> `'hello'` |
| `s.lstrip()` | Removes leading (left) whitespace. | `'  hello  '.lstrip()` -> `'hello  '` |
| `s.rstrip()` | Removes trailing (right) whitespace. | `'  hello  '.rstrip()` -> `'  hello'` |

### Search and Replace Methods
| Method | Description | Example |
| :--- | :--- | :--- |
| `s.replace(old, new)` | Returns a new string with all occurrences of `old` substring replaced by `new`. | `'banana'.replace('a', 'o')` -> `'bonono'` |
| `s.count(sub)` | Returns the number of non-overlapping occurrences of `sub` in the string. | `'banana'.count('a')` -> `3` |
| `s.find(sub)` | Returns the lowest index in the string where `sub` is found. Returns `-1` if not found. | `'Python'.find('o')` -> `4` |
| `s.index(sub)` | Similar to `find()`, but raises a `ValueError` if `sub` is not found. | `'Python'.index('o')` -> `4` |

---

## 7. Split and Join (Exam Favorite)

### `split()`
Splits a string into a list of substrings based on a delimiter. If no delimiter is specified, it splits by any whitespace and handles multiple spaces.

```python
text = "I love Python programming"
words = text.split(" ") # Split by single space
print(words)            # Output: ['I', 'love', 'Python', 'programming']

text_with_extra_spaces = "  Hello   World   Python  "
words_auto = text_with_extra_spaces.split() # Splits by any whitespace, handles multiple spaces
print(words_auto)       # Output: ['Hello', 'World', 'Python']
```

### `join()`
Concatenates a sequence of strings (e.g., a list of strings) into a single string, using the string on which the method is called as the separator.

```python
my_list_of_words = ['I', 'love', 'Python']
separator = "-"
new_sentence = separator.join(my_list_of_words)
print(new_sentence) # Output: 'I-love-Python'

another_sentence = " ".join(my_list_of_words)
print(another_sentence) # Output: 'I love Python'

# Join can also work on a string (iterates over characters)
print(",".join("abc")) # Output: 'a,b,c'
```

---

## 8. Looping Through Strings

```python
my_string = "Python"

# Basic for loop (iterates over characters)
for char in my_string:
    print(char)

# Looping with index and character using enumerate()
for index, char in enumerate(my_string):
    print(f"Index {index}: {char}")
```

---

## 9. String Formatting (Modern Approaches)

### F-strings (Formatted String Literals) - Recommended (Python 3.6+)
A concise and readable way to embed expressions inside string literals.

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 30 years old.

price = 19.99
print(f"The item costs ${price:.2f}.") # Formatting to 2 decimal places
# Output: The item costs $19.99.
```

### `str.format()` Method (Older, but still widely used)

```python
print("My name is {} and I am {} years old.".format("Bob", 25))
# Output: My name is Bob and I am 25 years old.

print("The item costs ${:.2f}.".format(24.5))
# Output: The item costs $24.50.
```

### `%` Operator (Oldest, C-style formatting - generally discouraged for new code)

```python
print("My name is %s and I am %d years old." % ("Charlie", 35))
# Output: My name is Charlie and I am 35 years old.
```

---

## 10. String vs. List (Quick Comparison)

| Feature         | String (`str`) | List (`list`) |
| :-------------- | :------------- | :------------ |
| **Mutable?**    | ❌ No          | ✅ Yes        |
| **Syntax**      | `""` or `''`   | `[]`          |
| **Ordered?**    | ✅ Yes         | ✅ Yes        |
| **Heterogeneous?** | ✅ Yes (characters) | ✅ Yes (elements) |
| **Change Element?** | ❌ (creates new) | ✅ (in-place) |

---

## 11. String Operations

### Concatenation (`+`)
Combines two or more strings.
```python
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
print(result) # Output: 'Hello World'
```

### Repetition (`*`)
Repeats a string a specified number of times.
```python
s = "Hi"
print(s * 3)    # Output: 'HiHiHi'
print(s * 0)    # Output: '' (empty string)
print(s * -2)   # Output: '' (empty string for negative multiplier)
```

### Membership (`in`, `not in`)
Checks if a substring exists within a string.
```python
text = "Python is fun"
print("Python" in text)    # Output: True
print("java" not in text)  # Output: True
```

### Comparison (`>`, `<`, `==`, `!=`, etc.)
Strings are compared character by character based on their ASCII/Unicode values.
```python
print("apple" > "banana")  # Output: False ('a' vs 'b')
print("A" > "a")           # Output: False (ASCII of 'A' is 65, 'a' is 97)
print("Python" == "python")# Output: False (case sensitive)
```

---

## 12. VVI Interview Questions & Tricks

### Q1. How to reverse a string in Python?
**Trick:** Use slicing with a step of `-1`.
```python
s = "Python"
reversed_s = s[::-1]
print(reversed_s) # Output: 'nohtyP'
```

### Q2. What does it mean that strings are immutable?
It means that once a string object is created, its content cannot be changed. Any operation that seems to modify a string (like `replace()`, `upper()`, or concatenation using `+`) actually creates a *new* string object in memory, leaving the original string untouched.

### Q3. How to check if a string contains only digits?
**Trick:** Use the `isdigit()` method.
```python
print("123".isdigit())   # Output: True
print("12.5".isdigit())  # Output: False (contains '.')
print("12a".isdigit())   # Output: False (contains 'a')
```

### Q4. Difference between `find()` and `index()`?
*   `find(sub)`: Returns the lowest index of the substring if found. Returns `-1` if not found.
*   `index(sub)`: Returns the lowest index of the substring if found. Raises a `ValueError` if not found.

```python
s = "hello"
print(s.find('l'))    # Output: 2
print(s.index('l'))   # Output: 2
print(s.find('z'))    # Output: -1
# print(s.index('z')) # Raises ValueError if uncommented
```

### Q5. How to remove duplicate characters from a string while preserving order?
**Trick:** Convert to a dictionary from keys (which preserves insertion order in Python 3.7+) and then join the keys.
```python
s = "programming"
unique_chars_ordered = "".join(dict.fromkeys(s))
print(unique_chars_ordered) # Output: 'progamin'
```

### Q6. Explain `is` vs `==` for strings.
*   `==` (Equality operator): Compares the **values** (content) of the strings.
*   `is` (Identity operator): Compares the **memory addresses** (references) of the strings.

Python often "interns" small, identical strings to save memory, making `is` return `True` for them. However, for dynamically created strings, `is` might return `False` even if `==` returns `True`.

```python
a = "hello"
b = "hello"
print(a == b) # True (values are the same)
print(a is b) # True (Python often interns these small strings)

c = "".join(["he", "llo"]) # Dynamically created
d = "hello"
print(c == d) # True (values are the same)
print(c is d) # False (likely different objects in memory)
```

### Q7. How to reverse each word in a sentence?
```python
sentence = "Hello World Python"
reversed_words_sentence = " ".join(word[::-1] for word in sentence.split())
print(reversed_words_sentence) # Output: 'olleH dlroW nohtyP'
```

### Q8. Palindrome Check (One-Liner)
```python
word = "madam"
is_palindrome = (word == word[::-1])
print(is_palindrome) # Output: True
```

---

## Conclusion
Strings are a fundamental and frequently used data type in Python. Understanding their immutable nature, indexing, slicing, and the rich set of built-in methods is crucial for effective text manipulation and programming in Python. Mastering these concepts will enable you to handle textual data efficiently and write robust code.
