# ---------------------------------------------------------
# Topic: Operations (Arithmetic, Relational, Type-Mixed)
# File: operations.py
# ---------------------------------------------------------

# --- 1. Arithmetic Operations ---
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Division: {a} / {b} = {a / b}")       # Float division
print(f"Floor Div: {a} // {b} = {a // b}")    # Integer division
print(f"Modulus: {a} % {b} = {a % b}")        # Remainder
print(f"Power: {a} ** {b} = {a ** b}")

# --- 2. Relational Operations ---
x = 100
y = 200

print(f"\nIs x equal to y? {x == y}")
print(f"Is x not equal to y? {x != y}")
print(f"Is x smaller? {x < y}")

# Chained comparison
age = 25
print(f"Is age valid (18-60)? {18 <= age <= 60}")

# --- 3. Same Type Operations ---
str1 = "Hello"
str2 = "World"
print(f"\nString Concat: {str1 + ' ' + str2}")

list1 = [1, 2]
list2 = [3, 4]
print(f"List Concat: {list1 + list2}")

# --- 4. Different Type Operations ---
text = "Python"
factor = 3
print(f"\nString Repetition: {text * factor}")

# Edge Case Handling
try:
    print("Result: " + 10)
except TypeError as e:
    print(f"\nError Caught: {e}")
    print("Fixed: " + "Result: " + str(10))
