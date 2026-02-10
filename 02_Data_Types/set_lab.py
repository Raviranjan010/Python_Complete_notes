"""
Sets Lab - Examples and Explanations
Covers: Union, Add, and Immutability requirements.
"""

# ==========================================
# 1. Union Operation
# ==========================================
a = {2, 3, 'Tina', 10+10j}
t = (10, 5)

# Error: set.union(t)
# Reason: 'set' is the class name. You must call union on an *instance* (object) of a set.
# Correct: a.union(t)
result = a.union(t)
print(f"Union result: {result}")


# ==========================================
# 2. Adding Elements
# ==========================================
# set.add() takes exactly one argument.
# The element must be IMMUTABLE (Hashable).

a.add(40)          # Valid (int is immutable)
a.add((2, 22))     # Valid (tuple is immutable)

# Error: a.add([1, 2])
# Reason: Lists are mutable. They cannot be hashed and stored in a set.

try:
    # Trying to add a set to a set (Sets are mutable too!)
    a.add({1, 2})
except TypeError as e:
    print(f"Cannot add mutable type to set: {e}")

print(f"Updated Set: {a}")
