# ---------------------------------------------------------
# Topic: Input and Output
# File: input_output.py
# ---------------------------------------------------------

# --- 1. Basic Input ---
name = input("Enter your name: ")
print(f"Hello, {name}!")

# --- 2. Numeric Input ---
# num = input("Enter a number: ") + 10 # Error
num_str = input("Enter a number to add 10 to: ")
num = int(num_str)
print(f"Result: {num + 10}")

# --- 3. Output Formatting (sep & end) ---
print("\n--- Output Formatting ---")
print("Python", "is", "awesome", sep="-") # Python-is-awesome

print("Loading", end="...")
print("Done!") # Loading...Done!

# --- 4. Multiple Inputs (One Line) ---
print("\n--- Multiple Inputs ---")
# Example: User enters "10 20"
data = input("Enter two numbers separated by space: ").split(" ")
# data is ["10", "20"] (List of strings)
a = int(data[0])
b = int(data[1])
print(f"Sum: {a + b}")
