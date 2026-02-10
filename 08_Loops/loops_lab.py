"""
Loops Lab - Examples and Explanations
Covers: while, for, nested loops, series, reversal, and patterns.
"""

# ==========================================
# 1. Number Series (While Loop)
# ==========================================
print("--- 1. Number Series ---")

# ==========================================
# 1. Number Series (While Loop)
# ==========================================
print("--- 1. Number Series ---")

# Q6. Series: 10, 20 ... 300
print("Q6: 10 to 300")
i = 10
while i <= 300:
    print(i, end=" ")
    i += 10
print() 

# Q7. Series: 105, 98 ... 7
print("Q7: 105 to 7")
i = 105
while i >= 7:
    print(i, end=" ")
    i -= 7
print()

# Q8. First 10 Natural Numbers Reverse
print("Q8: 10 to 1")
i = 10
while i >= 1:
    print(i, end=" ")
    i -= 1
print()

# Q9. Sum of First 10 Natural Numbers
print("\nQ9: Sum of first 10 Natural")
i = 1
s = 0
while i <= 10:
    s += i
    i += 1
print("Sum:", s)

# Q10. Sum of First 10 Even Numbers
print("Q10: Sum of first 10 Even")
i = 1
s = 0
count = 0
while count < 10:
    if i % 2 == 0:
        s += i
        count += 1
    i += 1
print("Sum:", s)

# ==========================================
# 1.1 Intermediate Termination (Password)
# ==========================================
print("\n--- Password Check (Infinite Loop) ---")
# while True:
#     n = input("Enter password (LPU@123): ")
#     if n == 'LPU@123':
#         print("Found")
#         break
#     else:
#         print("Wrong password. Try again.")
print("(Uncomment code to test Password Check)")

print("Reverse Series: 105, 98 ... 7")
i = 105
while i >= 7:
    print(i, end=" ")
    i -= 7
print()

# ==========================================
# 2. Summation Programs
# ==========================================
print("\n--- 2. Summation ---")

# Sum of First 10 Natural Numbers
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of 1-10: {total}")

# Sum of First 10 Even Numbers
ev_sum = 0
count = 0
num = 2
while count < 10:
    ev_sum += num
    num += 2
    count += 1
print(f"Sum of first 10 even numbers: {ev_sum}")

# ==========================================
# 3. String Manipulation
# ==========================================
print("\n--- 3. String Manipulation ---")

# Reverse String
s = "powerbi"
rev = ""
for char in s:
    rev = char + rev
print(f"Reversed '{s}': {rev}")

# Count Vowels
text = "My name is Anshuman"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Vowel count in '{text}': {count}")

# Mixed List Vowel Extraction (Try-Except Trick)
l_mixed = [10, 'programs', 'hello', True, 5.8]
extracted = []
for item in l_mixed:
    try:
        for char in item:
            if char in vowels:
                extracted.append(char)
    except TypeError:
        continue
print(f"Extracted vowels from mixed list: {extracted}")

# ==========================================
# 4. List Operations
# ==========================================
print("\n--- 4. List Operations ---")

# Largest Number
nums = [1, 23, 4, 6, 90, 67, 56]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print(f"Largest in {nums}: {largest}")

# Find Second Largest (Logic)
print("Finding Second Largest...")
vals = [10, 20, 50, 40, 50] # with duplicates
unique_vals = sorted(list(set(vals)))
if len(unique_vals) >= 2:
    print(f"Second largest: {unique_vals[-2]}")
else:
    print("List doesn't have enough unique elements.")

# ==========================================
# 5. Nested Loop - Reverse Words in List
# ==========================================
print("\n--- 5. Reverse Words ---")
words = ["hello", "python", "class"]
reversed_words = {}

for word in words:
    rev_w = ""
    for char in word:
        rev_w = char + rev_w
    reversed_words[word] = rev_w

print(f"Reversed Dictionary: {reversed_words}")

# ==========================================
# 6. Prime Number Check
# ==========================================
print("\n--- 6. Prime Check ---")
try:
    num = int(input("Enter number to check prime (e.g., 7): "))
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is NOT Prime")
                break
        else:
            print(f"{num} is Prime")
    else:
        print("Not Prime")
except ValueError:
    print("Invalid input")

# ==========================================
# 7. Additional Loop Questions (Q9-Q15)
# ==========================================
print("\n--- Additional Loop Exercises ---")

# Q9 & Q10: First 10 Even/Odd Numbers
print("First 10 Even Numbers:")
for i in range(0, 20, 2):
    print(i, end=" ")
print()

print("First 10 Odd Numbers:")
for i in range(1, 20, 2):
    print(i, end=" ")
print()

# Q13: Numbers and Squares
print("\nNumbers and Squares (1-10):")
for i in range(1, 11):
    print(f"{i} -> {i*i}")

# Q15: Pattern 1 1 2 2 ...
print("\nPattern 1 1 2 2 ... 10 10:")
for i in range(1, 11):
    print(f"{i} {i}", end=" ")
print()

# Star Pattern (Square)
print("\nSquare Star Pattern:")
n = 4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
