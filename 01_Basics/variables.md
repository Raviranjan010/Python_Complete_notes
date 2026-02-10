# Variables in Python

## 📦 What is a Variable?
A variable is like a **container** used to store data values.
Think of it as a labeled box where you can put stuff.

### Variable Space and Value Space
In Python, variables are not "boxes" that hold values in the traditional sense. Instead, they are **"labels" or "references"** that point to objects (values) in memory.

```python
a = 100
# Here, 'a' is a variable (identifier) that refers to the integer object '100' in memory.

b = a
# Now, 'b' also refers to the *same* integer object '100'.
# If 'a' changes to refer to a new object, 'b' will still refer to the original '100'
# (unless 'b' is also reassigned).
```
**Trick:** Use `id()` to see if two variables refer to the same object in memory.

---

## 🤹 Multiple Variable Creation
Python allows for convenient assignment of multiple variables:

*   **Multiple assignment:** Assign different values to different variables on one line.
    ```python
    a, b, c = 10, 20, 30
    print(f"a={a}, b={b}, c={c}") # Output: a=10, b=20, c=30
    ```
*   **Chained assignment:** Assign the same value to multiple variables.
    ```python
    x = y = z = 5
    print(f"x={x}, y={y}, z={z}") # Output: x=5, y=5, z=5
    ```

---


## 📝 Syntax
```python
variable_name = value
```
-   `=` is the assignment operator.
-   It assigns the value on the right to the variable name on the left.

## 🔄 Dynamic Typing
Python is **dynamically typed**, meaning you don't need to declare the type of a variable.
You can even change the type of data a variable holds later!

```python
x = 10      # x is an integer
x = "Hello" # Now x is a string (Perfectly valid in Python)
```

## 🚫 Rules for Naming Variables
1.  Must start with a **letter** (a-z, A-Z) or an **underscore** (_).
2.  Cannot start with a **number**.
3.  Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
4.  Case-sensitive (`age`, `Age` and `AGE` are different variables).
5.  Cannot use **Keywords** (reserved words like `if`, `else`, `class`).

---

### 🧠 Interview Point: Variable Assignment
**Q: What happens internally when you do `a = 10`?**
**A:**
1.  Python creates an integer object `10` in memory.
2.  Python creates the name `a`.
3.  Python makes `a` refer (point) to the object `10`.
*Variables in Python are references (labels) to objects, not the objects themselves.*
