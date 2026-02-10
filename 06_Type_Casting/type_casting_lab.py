"""
Type Casting Lab - Examples and Explanations
Covers: Fundamental type casting, Collection casting, Dictionary traps, and Common interview scenarios.
"""

# ==========================================
# 1. Fundamental Type Casting
# ==========================================
print("--- 1. Fundamental Type Casting ---")

# Integer Casting
print(f"int(3.99): {int(3.99)}")      # 3 (Truncated)
print(f"int(-2.5): {int(-2.5)}")      # -2
print(f"int(True): {int(True)}")      # 1
print(f"int('10'): {int('10')}")      # 10
# print(int("3.5"))  # ❌ ValueError
print(f"int(float('3.5')): {int(float('3.5'))}") # 3 (Workaround for string float)

# Boolean Casting
print(f"bool(0): {bool(0)}")          # False
print(f"bool('Hi'): {bool('Hi')}")    # True
print(f"bool('False'): {bool('False')}") # True (Non-empty string)
print(f"bool({{}}): {bool({})}")      # False (Empty dict)

# ==========================================
# 2. Collection Type Casting
# ==========================================
print("\n--- 2. Collection Type Casting ---")

s = "Python"
print(f"String to List: {list(s)}")   # ['P', 'y', 't', 'h', 'o', 'n']
print(f"String to Set: {set(s)}")     # Unique chars (Order random)

nums = [1, 2, 2, 3]
print(f"List to Set (Unique): {set(nums)}") # {1, 2, 3}

# ==========================================
# 3. Dictionary Casting (The Tricky Part)
# ==========================================
print("\n--- 3. Dictionary Casting ---")

# Valid Structures (Length 2 items)
l_valid = [[1, 'a'], [2, 'b']]
print(f"List of Lists -> Dict: {dict(l_valid)}") # {1: 'a', 2: 'b'}

t_valid = ('ab', 'xy')
print(f"Tuple of Strings -> Dict: {dict(t_valid)}") # {'a': 'b', 'x': 'y'}

# Invalid Structures
# dict(['abc']) # ❌ ValueError: length 3

# Duplicate Key Override
l_dup = [('a', 1), ('a', 2)]
print(f"Duplicate Keys: {dict(l_dup)}") # {'a': 2} (Last one wins)

# ==========================================
# 4. Lab Scenarios (From User Session)
# ==========================================
print("\n--- 4. Lab Scenarios ---")

# Tuple Casting
t1 = (2.3, 22, 2, 55, "RaviRaj", False)
print(f"Tuple: {t1}")
print(f"Tuple -> List: {list(t1)}")
# dict(t1) # ❌ TypeError NOT iterable pairs

# Set Casting
s1 = {1, 2, 3, 4, 5, 8, 9}
print(f"Set: {s1}")
# int(s1) # ❌ TypeError
print(f"Set -> List: {list(s1)}")
print(f"Set -> Str: {str(s1)}")

# Dictionary Casting
d1 = {'a': 10, 'b': 20, 'c': 30}
print(f"Dict: {d1}")
print(f"Dict -> Bool: {bool(d1)}") # True
print(f"Dict -> List (Keys): {list(d1)}")
print(f"Dict -> List (Values): {list(d1.values())}")
print(f"Dict -> List (Items): {list(d1.items())}")

# ==========================================
# 5. Common Traps
# ==========================================
print("\n--- 5. Common Traps ---")

# List to Dict directly?
list1 = [32, 4, 5, 5, 4]
# dict(list1) # ❌ Error
print("Direct List->Dict is Error. Needs pairs.")

# String 'False' to Bool
print(f"bool('False') is {bool('False')} (Startling but true!)")
