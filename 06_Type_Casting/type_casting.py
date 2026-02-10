# ---------------------------------------------------------
# Topic: Type Casting (Implicit and Explicit)
# File: type_casting.py
# ---------------------------------------------------------

# --- 1. Implicit Casting ---
x = 10      # int
y = 2.5     # float
z = x + y   # Python converts x to float, then adds
print(f"Value: {z}, Type: {type(z)}") # 12.5, float

# --- 2. Explicit Casting ---
s_num = "500"
i_num = int(s_num)
print(f"String '{s_num}' + 50 = {i_num + 50}")

# --- 3. Collection Casting ---
my_list = [1, 2, 2, 3]
my_set = set(my_list)   # Lists to Set (Removes duplicates)
print(f"List: {my_list} -> Set: {my_set}")

# --- 4. Input Handling (Crucial) ---
# input() always returns a string.
age = input("Enter your age (simulate): ") # Let's say user types 25
# if age > 18: -> TypeError
# Fix:
# if int(age) > 18: -> Correct

# --- 5. Data Loss ---
pi = 3.14159
print(f"Float: {pi} -> Int: {int(pi)}") # 3
