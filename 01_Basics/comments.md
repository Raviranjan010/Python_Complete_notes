# Comments in Python

## 💬 What are Comments?
Comments are lines of text in your code that are **ignored by the Python interpreter**.
They are used to explain the code to humans (developers) to make it more readable and maintainable.

## Types of Comments

### 1. Single-Line Comments
Start with a hash symbol (`#`). Everything after the `#` on that line is ignored.
```python
# This is a comment
print("Hello") # This is an inline comment
```

### 2. Multi-Line Comments
Python doesn't have a specific syntax for multi-line comments like `/* ... */` in C/Java.
However, we use **Docstrings** (Triple Quotes) or multiple `#` lines.

**Method A: Using Hash (#)**
```python
# This is a comment
# spanning multiple
# lines
```

**Method B: Using Docstrings (''' or """)**
```python
"""
This is a multi-line comment.
Usually used for documentation strings (docstrings)
inside functions or classes.
"""
```

---

### 🧠 Interview Point: Docstrings vs Comments
**Q: Are Docstrings ignored like comments?**
**A:** **No.**
-   **Comments (`#`)** are completely ignored by the interpreter.
-   **Docstrings (`"""..."""`)** are processed and associated with the object (like a function) as its `__doc__` attribute. They are used for documentation.
