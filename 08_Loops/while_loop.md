# While Loop

## Syntax
```python
while condition:
    # Code block
```
The loop continues **as long as** the condition is True.

## Example
```python
i = 1
while i < 6:
    print(i)
    i += 1
```

## ⚠️ Infinite Loops
If you forget to update the loop variable (like `i += 1`), the condition will remain True forever, causing an **Infinite Loop**.
```python
while True:
    print("This runs forever...")
    # Use Ctrl+C to stop
```
