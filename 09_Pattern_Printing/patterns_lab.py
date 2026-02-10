"""
Patterns Lab - Examples and Explanations
run this file to see various patterns
"""

n = 5 # Size for patterns

# ==========================================
# 1. Square Pattern
# ==========================================
print("\n--- 1. Square ---")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# ==========================================
# 2. Increasing Triangle
# ==========================================
print("\n--- 2. Increasing Triangle ---")
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

# ==========================================
# 3. Decreasing Triangle
# ==========================================
print("\n--- 3. Decreasing Triangle ---")
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

# ==========================================
# 4. Right Aligned Triangle
# ==========================================
print("\n--- 4. Right Aligned Triangle ---")
for i in range(1, n+1):
    print("  " * (n-i), end="")
    print("* " * i)

# ==========================================
# 5. Pyramid Pattern
# ==========================================
print("\n--- 5. Pyramid ---")
for i in range(1, n+1):
    print(" " * (n-i), end="") # Single space for tight pyramid
    for j in range(i):
        print("*", end=" ")
    print()

# ==========================================
# 6. Hollow Square
# ==========================================
print("\n--- 6. Hollow Square ---")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# ==========================================
# 7. Diamond Pattern
# ==========================================
print("\n--- 7. Diamond ---")
# Top
for i in range(1, n+1):
    print(" " * (n-i), end="")
    for j in range(i):
        print("*", end=" ")
    print()
# Bottom
for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")
    for j in range(i):
        print("*", end=" ")
    print()

# ==========================================
# 8. Number Triangle
# ==========================================
print("\n--- 8. Number Triangle ---")
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
