# For Loop

## Syntax
```python
for item in sequence:
    # Code block
```

## 1. Iterating over a List/String
```python
fruits = ["apple", "banana"]
for fruit in fruits:
    print(fruit)

for char in "Python":
    print(char)
```

## 2. The `range()` function
To loop through a set of code a specified number of times, we can use `range()`.
-   `range(n)`: 0 to n-1.
-   `range(start, stop)`: start to stop-1.
-   `range(start, stop, step)`: increment by step.

```python
for i in range(5):
    print(i) # 0, 1, 2, 3, 4
```
