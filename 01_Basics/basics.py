# ---------------------------------------------------------
# Topic: Variables, Keywords, Comments
# File: basics.py
# ---------------------------------------------------------

# --- 1. Variables ---
name = "Alice"      # String variable
age = 25            # Integer variable
height = 5.9        # Float variable
is_student = True   # Boolean variable

print("Name:", name)
print("Age:", age)

# --- 2. Dynamic Typing ---
# We can change the type of a variable
score = 100         # Int
print("Score is:", score)

score = "A+"        # Changed to String
print("Score is now:", score)

# --- 3. Keyword Check (Interview Question) ---
import keyword
print("\nList of all Python Keywords:")
print(keyword.kwlist)

# --- 4. Identifiers Edge Cases ---
# 1variable = 10     # ERROR: Cannot start with a number
# my-variable = 10   # ERROR: Hyphens are not allowed (interpreted as minus)
# class = 10         # ERROR: Cannot use keyword as variable name

my_variable = 10     # Valid (Snake Case)
_private_var = 20    # Valid (Starting with underscore is okay)

# --- 5. Multiple Assignment ---
x, y, z = 1, 2, 3
print("\nx:", x, "y:", y, "z:", z)

a = b = c = 100
print("a:", a, "b:", b, "c:", c)
