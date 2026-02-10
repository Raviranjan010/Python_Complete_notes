"""
Conditional Statements Lab - Examples and Explanations
"""

# ==========================================
# 1. Special Character Check
# ==========================================
ch = input("Enter a character to check if special: ")
if not ch.isalnum():
    print("Special Character")
else:
    print("Not a Special Character")

# ==========================================
# 2. Reverse String with Condition
# ==========================================
# Reverse string if it starts with uppercase and ends with digit
s = input("Enter a string for reverse check: ")
if s[0].isupper() and s[-1].isdigit():
    print(f"Reversed: {s[::-1]}")
else:
    print("Condition not satisfied (Must start with Upper and end with Digit)")

# ==========================================
# 3. Greatest of Three Numbers
# ==========================================
print("\n--- Greatest of 3 ---")
try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))

    if a >= b and a >= c:
        print("Greatest:", a)
    elif b >= a and b >= c:
        print("Greatest:", b)
    else:
        print("Greatest:", c)
except ValueError:
    print("Please enter valid integers.")

# ==========================================
# 4. Second Greatest of Four Numbers
# ==========================================
print("\n--- Second Greatest of 4 ---")
try:
    nums = []
    for i in range(4):
        nums.append(int(input(f"Enter number {i+1}: ")))
    nums.sort()
    print("Second Greatest:", nums[-2])
except ValueError:
    print("Invalid input.")

# ==========================================
# 5. Student Grading System
# ==========================================
print("\n--- Grading System ---")
try:
    p = float(input("Enter percentage: "))
    if p < 0 or p > 100:
        print("Invalid Percentage")
    elif p >= 90:
        print("Grade: A+")
    elif p >= 75:
        print("Grade: A")
    elif p >= 60:
        print("Grade: B")
    elif p >= 40:
        print("Grade: C")
    else:
        print("Result: Fail")
except ValueError:
    print("Invalid input.")

# ==========================================
# 6. Quadrant Check
# ==========================================
print("\n--- Quadrant Check ---")
try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    if x > 0 and y > 0:
        print("1st Quadrant")
    elif x < 0 and y > 0:
        print("2nd Quadrant")
    elif x < 0 and y < 0:
        print("3rd Quadrant")
    elif x > 0 and y < 0:
        print("4th Quadrant")
    else:
        print("On Axis or Origin")
except ValueError:
    print("Invalid input.")

# ==========================================
# 7. Number of Digits
# ==========================================
print("\n--- Digit Count ---")
try:
    n = abs(int(input("Enter a number: ")))
    if n < 10:
        print("Single Digit")
    elif n < 100:
        print("Double Digit")
    elif n < 1000:
        print("Triple Digit")
    else:
        print("More than 3 digits")
except ValueError:
    print("Invalid input.")

# ==========================================
# 8. FIZZ BUZZ
# ==========================================
print("\n--- FIZZ BUZZ ---")
try:
    n = int(input("Enter a number: "))
    if n % 15 == 0: # Check 15 first (divisible by 3 and 5)
        print("FIZZBUZZ")
    elif n % 3 == 0:
        print("FIZZ")
    elif n % 5 == 0:
        print("BUZZ")
    else:
        print(n)
except ValueError:
    print("Invalid input.")
