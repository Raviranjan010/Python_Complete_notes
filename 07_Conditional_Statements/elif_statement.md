# Elif Statement (Ladder)

The `elif` (short for "else if") statement is used when we have multiple conditions to check.

## Syntax
```python
if condition1:
    # Block 1
elif condition2:
    # Block 2
elif condition3:
    # Block 3
else:
    # Default Block
```

## Example
```python
marks = 85

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
else:
    grade = 'F'
```

### 🧠 Interview Point: Order Matters
Python checks conditions from **top to bottom**. Once it finds a `True` condition, it executes that block and **skips the rest**.
If `marks = 95` matches the first `if`, it won't check `elif marks >= 80`.
