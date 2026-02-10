# Try, Except, Else, Finally

## 1. `try` and `except`
Put risky code in `try`. Put error handling code in `except`.
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

## 2. `else` (Optional)
Executes if **NO** exception occurred.
```python
try:
    print("Hello")
except:
    print("Error")
else:
    print("Success, no error!")
```

## 3. `finally` (Optional)
Executes **ALWAYS**, regardless of whether an exception occurred or not.
Useful for cleaning up resources (closing files/connections).
```python
try:
    # Code
except:
    # Handle
finally:
    print("Job Done")
```
