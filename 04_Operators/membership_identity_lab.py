"""
Membership & Identity Operators Lab
Covers: 'in', 'not in', 'is', 'is not'
"""

# ==========================================
# 1. Membership Operators (in / not in)
# ==========================================
print("--- 1. Membership Operators ---")

# Lists
l = [10, 20, 30]
print(f"10 in {l}: {10 in l}")
print(f"1 in {l}: {1 in l}")

# Sets
s = {10, 20, 30}
print(f"10 in {s} (Set): {10 in s}")

# Strings
text = "Hello Python"
print(f"'Python' in '{text}': {'Python' in text}")
print(f"'z' in '{text}': {'z' in text}")

# Dictionaries (Checks Keys)
d = {'a': 1, 'b': 2}
print(f"'a' in {d}: {'a' in d}")
print(f"1 in {d}: {1 in d} (Checks keys only)")


# ==========================================
# 2. Identity Operators (is / is not)
# ==========================================
print("\n--- 2. Identity Operators ---")

# Integers (Small Integer Caching)
a = 10
b = 10
print(f"a=10, b=10 -> a is b: {a is b}")

# Lists (Mutable - Always new object)
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(f"l1={l1}, l2={l2}")
print(f"l1 == l2: {l1 == l2} (Values equal)")
print(f"l1 is l2: {l1 is l2} (Identity different)")

# Variables pointing to same object
c = a
print(f"c=a -> a is c: {a is c}")
