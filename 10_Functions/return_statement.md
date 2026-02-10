# Return Statement

The `return` statement is used to:
1.  Exit a function.
2.  Send a value back to the caller.

## Returning Multiple Values
Python has a super-power: **Comparing to other languages, Python functions can return multiple values.**
Internally, it returns a **Tuple**.

```python
def get_stats(numbers):
    return min(numbers), max(numbers)

low, high = get_stats([1, 2, 3])
```

## Returning None
If a function doesn't have a `return` statement, it implicitly returns `None`.
