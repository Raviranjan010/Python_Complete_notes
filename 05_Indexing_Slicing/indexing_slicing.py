# ---------------------------------------------------------
# Topic: Indexing and Slicing
# File: indexing_slicing.py
# ---------------------------------------------------------

data = "PythonProgramming"

# --- 1. Indexing ---
print(f"Original: {data}")
print(f"First char (0): {data[0]}")
print(f"Last char (-1): {data[-1]}")

# --- 2. Slicing Basics ---
print(f"\nSlice [0:6]: {data[0:6]}") # 'Python'
print(f"Slice [6:]:  {data[6:]}")  # 'Programming'

# --- 3. Step Slicing ---
print(f"Everything: {data[:]}")
print(f"Step 2:     {data[::2]}")  # PtoPormig

# --- 4. Reversing ---
reversed_data = data[::-1]
print(f"Reversed:   {reversed_data}")

# --- 5. List Slicing ---
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = numbers[2:8:2] # Start at 2, Stop before 8, Step 2 -> [2, 4, 6]
print(f"\nNumbers: {numbers}")
print(f"Sublist: {sub_list}")

# --- 6. Modification via Slicing ---
# You can replace chunks of lists using slicing!
my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [8, 9] # Replace index 1,2 with 8,9
print(f"Replaced List: {my_list}") # [1, 8, 9, 4, 5]
