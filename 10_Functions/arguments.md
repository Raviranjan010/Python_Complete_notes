# Function Arguments in Python

Python supports several types of arguments for functions.

## 1. Positional Arguments
Arguments are passed in the correct order.
```python
def f_name(name, mail, phone):
    print(name, mail, phone)

# Order matters!
f_name("Ravi", "ravi@email.com", 9876543210) 
```

## 2. Keyword Arguments
Arguments are passed by parameter name, so order doesn't matter.
```python
f_name(mail="ravi@gmail.com", phone=123, name="Ravi")
```

## 3. Default Arguments
Parameters assume a default value if not provided in the function call.
```python
def greet(name="User"):
    print(f"Hello, {name}")

greet()      # Uses default "User"
greet("Sam") # Uses "Sam"
```

## 4. Variable Length Arguments (`*args`)
Used when you don't know how many arguments will be passed.
*   collects arguments into a **Tuple**.
*   **Syntax**: `*args` (Formal Argument)

```python
def add_all(*nums):
    print(type(nums)) # <class 'tuple'>
    total = 0
    for n in nums:
        total += n
    print("Sum:", total)

add_all(10, 20, 30, 40)
```

## 5. Keyword Variable Length Arguments (`**kwargs`)
Used for passing variable number of keyword arguments.
*   collects arguments into a **Dictionary**.
*   **Syntax**: `**kwargs`

```python
def student_info(**details):
    print(type(details)) # <class 'dict'>
    print(details)

student_info(name="Ravi", course="Python", marks=90)
```

## 6. Mixed Arguments (Packing)
You can combine all types.
**Order Rule**: Positional -> `*args` -> Default -> `**kwargs`

```python
def master_func(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

master_func(1, 2, 3, 4, 5, mode="debug", status="active")
```

## 🔍 Unpacking Arguments
You can unpack a list/tuple into arguments using `*`.

```python
def un(a, b, c):
    print(a, b, c)

vals = (10, 20, 30)
un(*vals) # Equivalent to un(10, 20, 30)
```

## ⚠️ Interview Trap: Mutable Default Arguments
**Never use a mutable object (like a list or dict) as a default argument.**

### The Problem
```python
def add_item(item, l=[]):
    l.append(item)
    return l

print(add_item(1)) # [1]
print(add_item(2)) # [1, 2] (Wait, what? I wanted a new list!)
```
**Reason**: Default arguments are evaluated **only once** when the function is defined, not every time it's called. The same list `l` is shared across calls.

### The Fix
Use `None` as the default value.
```python
def add_item(item, l=None):
    if l is None:
        l = []  # Create a new list every time
    l.append(item)
    return l

print(add_item(1)) # [1]
print(add_item(2)) # [2] (Correct!)
```
