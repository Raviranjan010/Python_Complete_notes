# ---------------------------------------------------------
# Topic: Pattern Printing
# File: patterns.py
# ---------------------------------------------------------

n = 5 # Size

# --- 1. Right Triangle ---
print("--- Right Triangle ---")
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print() # Newline after each row

# --- 2. Inverted Triangle ---
print("\n--- Inverted Triangle ---")
for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()

# --- 3. Number Pyramid (Increasing) ---
print("\n--- Number Pyramid ---")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# --- 4. Pyramid (Centered) ---
print("\n--- Centered Pyramid ---")
#    *
#   * *
#  * * *
for i in range(n):
    # Print spaces
    print(" " * (n - i - 1), end="")
    # Print stars
    print("* " * (i + 1))
