# ---------------------------------------------------------
# Topic: Operators (Logical, Assignment, Membership, Identity)
# File: operators.py
# ---------------------------------------------------------

# --- 1. Logical Operators ---
t = True
f = False

print(f"True and False: {t and f}")
print(f"True or False: {t or f}")
print(f"Not True: {not t}")

# Short-circuit demo (Safe division)
x = 0
# y = 10 / x  # This would crash
# But this is safe:
(x != 0) and print(10 / x) # Second part skipped because x!=0 is False

# --- 2. Membership Operators ---
print("\n--- Membership ---")
menu = ["Pizza", "Burger", "Pasta"]
order = "Burger"

if order in menu:
    print(f"{order} is available!")
else:
    print(f"{order} is not on the menu.")

# --- 3. Identity Operators ---
print("\n--- Identity ---")
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x == y: {x == y} (Values are same)")
print(f"x is y: {x is y} (Objects are different)")
print(f"x is z: {x is z} (Same Object)")

# --- 4. Assignment Operators ---
print("\n--- Assignment ---")
count = 10
count += 5 # count = count + 5
print(f"Count after += 5: {count}")
count *= 2
print(f"Count after *= 2: {count}")
