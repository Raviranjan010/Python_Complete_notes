# Loop Control Statements

Statements that change the execution flow of a loop.

## 1. `break`
Stops the loop entirely and exits.
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Prints 0 to 4, then stops.
```

## 2. `continue`
Skips the **current** iteration and continues with the next one.
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
# Prints 0, 1, 3, 4 (Skips 2)
```

## 3. `pass`
Does nothing. Acts as a placeholder.
```python
for i in range(5):
    pass # Todo: Add logic later
```

## 4. `else` with Loops (Interview Point)
Python loops can have an `else` block!
The `else` block executes **after the loop finishes normally**.
**Important: It does NOT execute if the loop is stopped by a `break`.**
```python
for x in range(3):
    print(x)
else:
    print("Done!")
```
