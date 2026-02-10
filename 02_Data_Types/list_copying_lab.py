"""
List Copying Lab - Examples and Explanations
Covers: Assignment, Shallow Copy, and Deep Copy.
"""
import copy

# ==========================================
# 1. Assignment (Reference)
# ==========================================
l1 = [1, 2, 3]
l2 = l1  # Both point to same memory
l2[0] = 99
print(f"Assignment - l1: {l1}")  # [99, 2, 3] (Changed!)


# ==========================================
# 2. Shallow Copy (.copy())
# ==========================================
# Creates a new list, but inner elements are still references if they are mutable.
original = [1, 2, [100, 200]]
shallow = original.copy()

# Modifying outer element -> Independent
shallow[0] = 999

# Modifying inner element -> Affects BOTH
shallow[2][0] = 'Changed'

print(f"Shallow Original: {original}") # [1, 2, ['Changed', 200]]
print(f"Shallow Copy:     {shallow}")  # [999, 2, ['Changed', 200]]


# ==========================================
# 4. Common Errors & Traps (REPL Experiments)
# ==========================================
print("\n--- 4. Common Copying Traps ---")

# Trap 1: Variable Name Case Sensitivity
# L = [1, 2, 3]
# a = l.copy() -> NameError: name 'l' is not defined. Did you mean: 'L'?
try:
    L_temp = [1, 2, 3]
    # a = l_temp.copy() # Uncommenting this would crash
    print("Remember: Python is case-sensitive (L vs l)")
except NameError as e:
    print(e)

# Trap 2: Nested List Behavior in Shallow Copy
l2 = [1, 2, 3, [2, 3, 2], 7]
l4 = l2.copy()
l4[3][0] = 99
print(f"Original after nested change: {l2}") # [..., [99, 3, 2], ...]
print(f"Copy after nested change:     {l4}") # [..., [99, 3, 2], ...]
print("-> Nested lists are SHARED in shallow copy!")
