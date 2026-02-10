"""
Operators Lab - Examples and Explanations
Covers: Relational, Logical, and Identity operators.
"""

# ==========================================
# 1. Relational Operators (Comparison)
# ==========================================
print("--- 1. Relational Operators ---")

# --- Strings ---
# Comparison is based on ASCII/Unicode values.
# 'A' (65) < 'a' (97)
print(f"'Amaan' > 'Anshuman': {'Amaan' > 'Anshuman'}") # False ('m' < 'n')
print(f"'Python' > 'Hello': {'Python' > 'Hello'}")     # True ('P' > 'H')

# --- Lists ---
# Comparison is element-by-element.
# [10, 20] > [1, 2] -> True because 10 > 1.
print(f"[10, 20] > [1, 2]: {[10, 20] > [1, 2]}")

# [10, 20] > [10, 20] -> False (They are equal)

# --- Equality Traps ---
# (10) is an int. (10,) is a tuple.
print(f"10 == (10): {10 == (10)}")    # True
print(f"10 == (10,): {10 == (10,)}")  # False


# ==========================================
# 2. Logical Operators (and / or)
# ==========================================
print("\n--- 2. Logical Operators ---")
# Python returns the *value* that decided the result, not just True/False.

# AND: Returns first Falsy value, or the last value if all are True.
print(f"10 and 0: {10 and 0}")       # 0
print(f"10 and 20: {10 and 20}")     # 20

# OR: Returns first Truthy value, or the last value if all are False.
print(f"10 or 0: {10 or 0}")         # 10
print(f"0 or 'Hi': {0 or 'Hi'}")     # 'Hi'


# ==========================================
# 3. Identity Operators (is)
# ==========================================
print("\n--- 3. Identity Operators ---")
a = 10
b = 10
print(f"a is b: {a is b}")  # True (Small integers are cached)

l1 = [1, 2]
l2 = [1, 2]
print(f"l1 is l2: {l1 is l2}") # False (Different memory locations)
print(f"l1 == l2: {l1 == l2}") # True (Values are same)


# ==========================================
# 4. Arithmetic & Complex
# ==========================================
print("\n--- 4. Arithmetic & Complex ---")
c = 3 + 4j
print(f"Complex math (3+4j)*3: {c * 3}")
print(f"True / 2: {True / 2}")  # 0.5 (True acts as 1)

# Advanced Arithmetic
print(f"10 // 3: {10 // 3}")   # 3
print(f"10 % 3: {10 % 3}")    # 1
print(f"10 / 3: {10 / 3}")    # 3.33...
