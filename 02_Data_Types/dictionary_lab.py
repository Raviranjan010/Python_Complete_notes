"""
Dictionary Lab - Examples and Explanations
Covers: Creation, Key Overriding, Nested Access, and Common Errors.
"""

# ==========================================
# 1. Key Overriding
# ==========================================
# If a key is repeated, the LAST value wins.
# Note: True and 1 are treated as the same key in hashing.
d2 = {True: 33, 2: False}
print(f"d2: {d2}")  # {True: 33, 2: False}

d3 = {1: 33, "a": "Acsa", 5: 43}
print(f"d3 type: {type(d3)}")

# ==========================================
# 2. Accessing Elements
# ==========================================
print(f"d3['a']: {d3['a']}")

# Error: Accessing by index (Dictionaries are not ordered by index like lists)
try:
    print(d3[3])
except KeyError as e:
    print(f"Error accessing d3[3]: {e} (Key not found)")

# Nested String Indexing
# d3['a'] is 'Acsa'. We can index the string.
print(f"d3['a'][2]: {d3['a'][2]}")  # 's'


# ==========================================
# 3. Complex Nesting & Sets
# ==========================================
# d4 = { ... 'a':{(2.2),(20+2j), 10} ... }
# Note: {10} is a set. (10) is an int. (10,) is a tuple.

d4 = {
    1: 10, 
    2: 2.25, 
    2.2: 3+22j, 
    4: False, 
    'a': {2.2, 10, (20+2j)},  # Set (Unordered)
    'b': ['Hi', 10]           # List (Ordered)
}

# Fetching 'Hi'
print(f"From list: {d4['b'][0]}")

# Fetching 2.2 from the set at d4['a']
# ERROR REASON: Sets are unordered. You cannot use index [0].
# You must iterate or check membership.
print(f"Set content: {d4['a']}")

# ==========================================
# 4. Modification
# ==========================================
d = {1: 'Das', 2: 4}
d[1] = "Alia"    # Update
d[7] = 'Thala'   # Add new
d.pop(1)         # Remove key 1
print(f"Final d: {d}")
