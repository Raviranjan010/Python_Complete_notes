# ---------------------------------------------------------
# Topic: Loops (for, while, range, break, continue)
# File: loops.py
# ---------------------------------------------------------

# --- 1. For Loop with Range ---
print("--- Range(5) ---")
for i in range(5):
    print(i, end=" ") # 0 1 2 3 4
print()

# --- 2. Iterating Collection ---
print("\n--- Iterating List ---")
colors = ["Red", "Green", "Blue"]
for color in colors:
    print(f"Color: {color}")

# --- 3. While Loop ---
print("\n--- While Loop ---")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Blastoff!")

# --- 4. Break Statement ---
print("\n--- Break Demo ---")
# Find the first even number greater than 3
for num in [1, 3, 5, 8, 9]:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break # Exit loop immediately

# --- 5. Continue Statement ---
print("\n--- Continue Demo ---")
# Print only odd numbers
for i in range(6):
    if i % 2 == 0:
        continue # Skip even numbers
    print(i, end=" ") # 1 3 5

# --- 6. Loop Else (Interview Trick) ---
print("\n\n--- Loop Else ---")
# Check if a number is prime
n = 7
for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not prime.")
        break
else:
    # Executed ONLY if loop didn't break
    print(f"{n} is prime!")
