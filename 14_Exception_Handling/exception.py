# ---------------------------------------------------------
# Topic: Exception Handling
# File: exception.py
# ---------------------------------------------------------

# --- 1. Basic Try-Except ---
print("--- Division Calculator ---")
try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Divison by zero is not allowed.")

except ValueError:
    print("Error: Please enter a valid number.")

except Exception as e:
    # Generic catch-all
    print(f"Unknown Error: {e}")

# --- 2. Try-Except-Else-Finally ---
print("\n--- File Operations (Simulation) ---")
try:
    print("Opening File...")
    # Simulate file op
    content = "File Data" 
    # raise Exception("Disk Full") # Uncomment to test error
except Exception as e:
    print(f"Error reading file: {e}")
else:
    print("File read successfully.")
finally:
    print("Closing File...") # Always runs
