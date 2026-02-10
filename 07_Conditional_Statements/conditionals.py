# ---------------------------------------------------------
# Topic: Conditional Statements (if, elif, else)
# File: conditionals.py
# ---------------------------------------------------------

# --- 1. Basic If-Else ---
number = 7
print(f"Checking number: {number}")

if number % 2 == 0:
    print("It is Even.")
else:
    print("It is Odd.")

# --- 2. Elif Ladder ---
score = 85
print(f"\nScore: {score}")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")

# --- 3. Nested If ---
print("\n--- Nested If ---")
num = 15

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive Number")
else:
    print("Negative Number")

# --- 4. Short Hand If-Else (Ternary Operator) ---
# Syntax: value_if_true if condition else value_if_false
status = "Adult" if 20 >= 18 else "Minor"
print(f"\nStatus: {status}")
