# Output Methods

## The `print()` Function
Used to display output to the console.

## Parameters
1.  **`object(s)`**: Values to be printed.
2.  **`sep`**: Separator between values (default is space `" "`).
3.  **`end`**: What to print at the end (default is newline `"\n"`).

## Examples
```python
print("Hello", "World") # Default sep=" " -> Hello World

print("Hello", "World", sep="-") # Hello-World

print("Hello", end=" ") # Stays on same line
print("World")          # Hello World
```

## F-Strings (Formatted Strings)
The best way to output variables.
```python
name = "Sam"
print(f"Hello {name}")
```
