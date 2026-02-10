"""
Functions Lab - Examples and Explanations
Covers: Basic, Arguments, Return, Recursion, Packing/Unpacking, and Calculator.
"""

# ==========================================
# 1. Basic Function & Types
# ==========================================
print("\n--- 1. Basic Functions ---")

def sum_basic():
    # Function with no arguments and return (Simulated input)
    print("Function called")
    return

# Call
print(sum_basic()) # Returns None

def sum_args(a, b):
    return a + b
print(f"Sum (78, 86): {sum_args(78, 86)}")

# ==========================================
# 2. Palindrome Extractor (List Manipulation)
# ==========================================
print("\n--- 2. Palindrome Extractor ---")
def extract_palindromes(L):
    pal = []
    for i in L:
        # Check if type is string AND if it matches its reverse
        if type(i) == str and i == i[::-1]:
            pal.append(i)
    print(f"Palindromes in {L}: {pal}")

data = [145, 2+3j, "NAYAN", "HI", "MADAM"]
extract_palindromes(data)

# ==========================================
# 3. List Concatenation (Without + Operator)
# ==========================================
print("\n--- 3. List Concatenation ---")
def concatenate_lists(l1, l2):
    # Method 1: Using extend
    # result = l1.copy()
    # result.extend(l2)
    
    # Method 2: Manual append
    out = l1.copy()
    for i in l2:
        out.append(i)
    return out

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(f"Concat {l1} + {l2} = {concatenate_lists(l1, l2)}")

# ==========================================
# 4. Calculator (Nested Functions)
# ==========================================
print("\n--- 4. Calculator ---")
def calculator():
    print("Calculator started (Press 5 to Exit)")
    while True:
        try:
            choice = input("\nSelect operation (1:Add, 2:Sub, 3:Mul, 4:Div, 5:Exit): ")
            
            if choice == "5":
                print("Thank you!")
                break
                
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            def add(): return a + b
            def sub(): return a - b
            def mul(): return a * b
            def div():
                if b == 0: return "Error: Division by zero!"
                return a / b

            if choice == "1":
                print(f"Result: {add()}")
            elif choice == "2":
                print(f"Result: {sub()}")
            elif choice == "3":
                print(f"Result: {mul()}")
            elif choice == "4":
                print(f"Result: {div()}")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid Input! Please enter numbers.")

# Uncomment to run
# calculator()

# ==========================================
# 5. Packing and Unpacking (*args, **kwargs)
# ==========================================
print("\n--- 5. Packing & Unpacking ---")

# Tuple Packing (*args)
def tuple_packing(*args):
    print(f"Packed Args (Tuple): {args}, Type: {type(args)}")

tuple_packing(10, 20, 30)

# Dictionary Packing (**kwargs)
def dict_packing(**kwargs):
    print(f"Packed Kwargs (Dict): {kwargs}, Type: {type(kwargs)}")

dict_packing(name="Ravi", role="Developer")

# Mixed Packing
def mixed_packing(*args, **kwargs):
    print(f"Args: {args}, Kwargs: {kwargs}")

mixed_packing(1, 2, 3, a="A", b="B")

# Unpacking
print("\n--- Unpacking ---")
def show_values(a, b, c):
    print(f"a={a}, b={b}, c={c}")

vals = (10, 20, 30)
show_values(*vals) # Unpacking tuple into arguments

# ==========================================
# 6. Factorial (Recursion vs Iteration)
# ==========================================
print("\n--- 6. Factorial ---")
def fact(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    print(f"Factorial of {n} is {res}")

# input_n = int(input("Enter num for factorial: "))
# fact(input_n)
fact(5)

# ==========================================
# 7. Advanced Packing & Unpacking Rules
# ==========================================
print("\n--- 7. Advanced Packing Details ---")

# 1. Unpacking Lists/Tuples/Strings
def unpack_demo(a, b, c):
    print(f"Unpacked: {a}, {b}, {c}")

print("Unpacking Tuple:")
unpack_demo(*(1, 2, 3))

print("Unpacking List:")
unpack_demo(*[10, 20, 30])

print("Unpacking String (Each char):")
unpack_demo(*"ABC")

# 2. Variable Arguments with Type Check
def flexible_args(*args):
    print(f"Received {args} of type {type(args)}")

flexible_args(1, 2, 3)

# 3. Dictionary Unpacking
def dict_demo(x, y):
    print(f"Dict Unpack: x={x}, y={y}")

d_vals = {'x': 100, 'y': 200}
dict_demo(**d_vals) # Keys must match argument names!
