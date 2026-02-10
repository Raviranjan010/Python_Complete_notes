"""
Slicing Lab - Examples and Explanations
Covers: List slicing, String slicing, Negative indexing, and Nested slicing.
"""

# ==========================================
# 1. Basic List Slicing
# ==========================================
print("--- 1. Basic List Slicing ---")
a = [10, 20, 30, 40, 50]

# Positive Slicing [start : end]
# Start is inclusive, End is exclusive.
print(f"Original List: {a}")
print(f"a[1:4]: {a[1:4]}")  # Output: [20, 30, 40]

# Negative Slicing
# Indices: -5(10), -4(20), -3(30), -2(40), -1(50)
print(f"a[-4:-1]: {a[-4:-1]}")  # Output: [20, 30, 40]


# ==========================================
# 2. String Slicing & Direction Rules
# ==========================================
print("\n--- 2. String Slicing & Direction Rules ---")
s = 'Dictionary'

# Full string
print(f"Full: {s[::1]}")

# Reverse string
print(f"Reverse: {s[::-1]}")  # 'yranoitciD'

# --- The "Empty String" Trap ---
# s[-1:-4]
# Start: -1 ('y'), End: -4 ('n').
# Default Step: +1 (Moves Left -> Right).
# Reason: You cannot go from -1 (Right) to -4 (Left) using a positive step.
print(f"s[-1:-4] (Empty): '{s[-1:-4]}'")

# --- The Fix: Negative Step ---
# To move backwards, step must be negative.
print(f"s[-1:-4:-1]: '{s[-1:-4:-1]}'")  # 'yra'
print(f"s[-4:-1]: '{s[-4:-1]}'")        # 'nar' (Standard left-to-right using negative indices)

# Advanced Step
s2 = 'Dictionary'
# Start -1, End -10, Step -2 (Skip every 2nd char backwards)
print(f"s2[-1:-10:-2]: {s2[-1:-10:-2]}")  # 'yaoti'


# ==========================================
# 3. Nested Slicing (Deep Access)
# ==========================================
print("\n--- 3. Nested Slicing (Deep Access) ---")
s3 = ['Hello class', (5.2+2.36j, 11, False), {'a': 101, 10.1: 5500}]

# Goal: Fetch reverse of the tuple at index 1
# s3[1] is (5.2+2.36j, 11, False)
# [::-1] reverses it.
rev = s3[1][::-1]
print(f"Reverse tuple: {rev}")

# Complex Nested Structure
s7 = {'a': ["This is a list"], 'b': [10, 20, 30, ("Hello", 'Guys')]}

# Goal: Fetch reverse of 'Guys'
# Path:
# 1. s7['b']       -> [10, 20, 30, ("Hello", 'Guys')]
# 2. [3]           -> ("Hello", 'Guys')
# 3. [1]           -> 'Guys'
# 4. [::-1]        -> 'syuG'
print(f"Reverse 'Guys': {s7['b'][3][1][::-1]}")

# List inside List
l6 = [1, 2.2, [2+2j, True, ['Yadav ji', 'Pandey Ji', False]]]
# Access 'Pandey Ji'
# l6[2] -> Inner list
# [2]   -> Innermost list
# [1]   -> 'Pandey Ji'
print(f"Nested Access: {l6[2][2][1]}")
