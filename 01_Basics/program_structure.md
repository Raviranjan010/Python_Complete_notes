# 🔰 Python Program Structure & Important Characteristics

---

## Python Program Structure
A basic Python program consists of:
*   **Statements:** Instructions that the Python interpreter can execute.
*   **Indentation instead of `{}`:** Python uses whitespace (spaces or tabs) to define code blocks (e.g., within `if` statements, `for` loops, functions, classes). This enforces readability.
*   **Comments using `#`:** Used to explain code and make it more understandable.

```python
# This is a single-line comment.
# Any text after '#' on the same line is ignored by the interpreter.

"""
This is a multi-line comment,
also known as a docstring when placed at the beginning of a module,
function, class, or method. It's actually a string literal,
but if not assigned to a variable, it acts as a comment.
"""

# Example of a simple Python program
name = "World"  # Assigning a string value to a variable
if name == "World":
    print(f"Hello, {name}!") # Indented block for the if statement
else:
    print("Hello, stranger!")
```
**Point to Remember:** Consistent indentation is crucial. Mixing tabs and spaces can lead to `IndentationError`s. PEP 8 recommends 4 spaces per indentation level.

---

## Important Characteristics
*   **Case-sensitive language:** `myVariable` is different from `myvariable`.
    ```python
    myVar = 10
    MyVar = 20
    print(myVar) # Output: 10
    print(MyVar) # Output: 20
    ```
*   **Indentation is mandatory:** Defines code blocks. Incorrect indentation will result in an `IndentationError`.
*   **No semicolon required:** Unlike C++ or Java, statements typically do not end with a semicolon. You *can* use it to put multiple statements on one line, but it's generally discouraged for readability.
    ```python
    # Discouraged:
    a = 10; b = 20; print(a + b)

    # Preferred:
    a = 10
    b = 20
    print(a + b)
    ```
*   **Supports interactive mode:** You can type Python commands directly into the interpreter and get immediate results. This is excellent for testing and learning.
