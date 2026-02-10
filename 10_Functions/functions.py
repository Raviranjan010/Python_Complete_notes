# ---------------------------------------------------------
# Topic: Functions
# File: functions.py
# ---------------------------------------------------------

# --- 1. Basic Function ---
def greet(name):
    """Docstring: This function greets the user."""
    return f"Hello, {name}!"

msg = greet("Alice")
print(msg)

# --- 2. Default Arguments ---
def power(number, exponent=2):
    return number ** exponent

print(f"5^2: {power(5)}")      # Uses default exponent=2
print(f"5^3: {power(5, 3)}")   # Overrides default

# --- 3. *args (Sum of ANY numbers) ---
def add_all(*args):
    """Sum arbitrary number of arguments"""
    result = 0
    for num in args:
        result += num
    return result

print(f"Sum: {add_all(1, 2, 3, 4, 10)}")

# --- 4. **kwargs (Dictionary inputs) ---
def print_details(**kwargs):
    print("\n--- Details ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Bob", age=30, job="Developer")

# --- 5. Returning Multiple Values ---
def calc(a, b):
    return a+b, a-b, a*b, a/b

summ, sub, mul, div = calc(10, 2)
print(f"\nResults -> +:{summ}, -:{sub}, *:{mul}, /:{div}")
