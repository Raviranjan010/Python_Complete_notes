# ---------------------------------------------------------
# Topic: Data Types (Numeric, Strings, Lists, Tuples, Sets, Dicts)
# File: data_types.py
# ---------------------------------------------------------

# --- 1. Integers & Floats ---
x = 10      # int
y = 3.14    # float
print(f"Type of x: {type(x)}")
print(f"Type of y: {type(y)}")

# --- 2. String Operations ---
s = "  Python Programming  "
print(f"Original: '{s}'")
print(f"Strip: '{s.strip()}'")
print(f"Lower: '{s.lower()}'")
print(f"Replace: '{s.replace('Python', 'Java')}'")

# Chain methods
clean_s = s.strip().upper()
print(f"Cleaned: {clean_s}")

# --- 3. Lists (Mutable) ---
print("\n--- Listing ---")
my_list = [1, 2, 3]
my_list.append(4)       # Add to end
my_list[0] = 100        # Modify first element
print(f"List: {my_list}")

# --- 4. Tuples (Immutable) ---
print("\n--- Tuples ---")
my_tuple = (1, 2, 3)
# my_tuple[0] = 100     # ERROR: TypeError: 'tuple' object does not support item assignment
print(f"Tuple: {my_tuple}")

single_element = (5,)   # Comma is important!
print(f"Single Tuple Type: {type(single_element)}")

# --- 5. Sets (Unique & Unordered) ---
print("\n--- Sets ---")
my_set = {1, 2, 3, 3, 3}
print(f"Set: {my_set}") # {1, 2, 3} - Duplicates removed

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
print(f"Union: {a | b}")        # {1, 2, 3, 4, 5}
print(f"Intersection: {a & b}") # {3}

# --- 6. Dictionaries (Key-Value) ---
print("\n--- Dictionaries ---")
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing
print(f"Name: {person['name']}")
print(f"Job: {person.get('job', 'Not Specified')}") # Safer access

# Modifying
person["age"] = 31      # Update
person["job"] = "Engineer" # Add new key
print(f"Updated Person: {person}")

# Keys and Values
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
