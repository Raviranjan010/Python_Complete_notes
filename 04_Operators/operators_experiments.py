# 🧪 Operators Lab Experiments (The "Perfect Detailed Notes")
# Contains: Relational, Logical, Membership, Identity, Arithmetic traps

# ==========================================
# 1. Relational Operators (String & List)
# ==========================================
print("\n--- 1. Relational Operators ---")

# String Comparison (ASCII Value)
print("'Amaan' > 'Anshuman':", 'Amaan' > 'Anshuman') # False ('A'=='A', 'm' < 'n')
print("'Python' > 'Hello':", 'Python' > 'Hello')     # True ('P' > 'H')
print("'Hello' > 'python':", 'Hello' > 'python')     # False ('H' < 'p')

# List Comparison (Element by Element)
print("[10,20,30] > [1,2,3]:", [10,20,30] > [1,2,3])       # True (10 > 1)
print("[10,20,30] > [1,30,40]:", [10,20,30] > [1,30,40])   # True (10>1)
print("[10,20,30] > [10,20,30]:", [10,20,30] > [10,20,30]) # False (Equal)

# Tricky Cases
# [10,20,30] > [1,20,40]: True
# [1,20,30] > [1,20,40]: False (30 < 40)

# Equality Traps
print("10 == (10):", 10 == (10))    # True
print("10 == (10,):", 10 == (10,))  # False (Int vs Tuple)
print("[10] != 10.0:", [10] != 10.0) # True (Types differ)
print("10 != 10.0:", 10 != 10.0)    # False (Values equal)

# ==========================================
# 1.1 Mixed Type Comparisons (REPL Errors)
# ==========================================
print("\n--- Mixed Type Errors (Try-Except) ---")
try:
    print("{3} > [3]")
    {3} > [3]
except TypeError as e:
    print(f"Error: {e}") # '>' not supported between instances of 'set' and 'list'

try:
    print("22 > [22]")
    22 > [22]
except TypeError as e:
    print(f"Error: {e}") # '>' not supported between instances of 'int' and 'list'

# ==========================================
# 1.2 Comparison Logic
# ==========================================
print("\n--- Detailed Comparison Logic ---")
print("'Amaan' > 'Anshuman':", 'Amaan' > 'Anshuman') # False (m < n)
print("ord('d') > 3:", ord('d') > 3) # True (100 > 3)


# ==========================================
# 2. Set Comparison (Subset/Superset)
# ==========================================
print("\n--- 2. Set Comparisons ---")
print("{1,3,4,5} > {1,2,3}:", {1,3,4,5} > {1,2,3}) # False (2 not in first)
print("{1,3,4,5} > {1,5,3}:", {1,3,4,5} > {1,5,3}) # True (Superset)

# Set Difference (Not Subtraction)
print("{22,33,4} - {22}:", {22,33,4} - {22})     # {33, 4}
print("{22,33,4} - {22,2}:", {22,33,4} - {22,2}) # {33, 4} (2 ignored)


# ==========================================
# 3. Logical Operators (Short-Circuit)
# ==========================================
print("\n--- 3. Logical Operators ---")
# AND: First Falsy or Last Value
print("10 and 0:", 10 and 0)         # 0
print("'Hi' and 'Hello':", 'Hi' and 'Hello') # 'Hello'
print("{} and 0.0:", {} and 0.0)     # {}

# OR: First Truthy or Last Value
print("10 or 2:", 10 or 2)           # 10
print("0 or 'hi':", 0 or 'hi')       # 'hi'
print("{} or 0.0:", {} or 0.0)       # 0.0

# NOT
print("not(0):", not(0))             # True
print("not('hi'):", not('hi'))       # False


# ==========================================
# 4. Identity Operators (is, is not)
# ==========================================
print("\n--- 4. Identity Operators ---")
a = 10
b = 20
c = 10
print(f"a={a}, b={b}, c={c}")
print("a is c:", a is c)         # True (Same object)
print("a is b:", a is b)         # False
print("a is not b:", a is not b) # True


# ==========================================
# 5. Membership Operators (in, not in)
# ==========================================
print("\n--- 5. Membership Operators ---")
print("10 in [10, 20, 30]:", 10 in [10, 20, 30]) # True
print("1 in [10, 20, 30]:", 1 in [10, 20, 30])   # False
print("1 not in {10, 20, 30}:", 1 not in {10, 20, 30}) # True


# ==========================================
# 6. Arithmetic & Complex
# ==========================================
print("\n--- 6. Arithmetic & Complex ---")
print("(3+4j)*3:", (3+4j)*3)   # (9+12j)
print("(3+4j)**2:", (3+4j)**2) # (-7+24j)
print("True / 2:", True / 2)   # 0.5
