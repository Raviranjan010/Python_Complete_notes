# Indexing

Indexing is used to access individual items in an ordered sequence (String, List, Tuple).

## 0-Based Indexing
Python uses 0-based indexing.
-   First element: Index `0`
-   Second element: Index `1`

## Negative Indexing
Python supports negative indexing to access elements from the **end**.
-   Last element: Index `-1`
-   Second last: Index `-2`

```python
s = "PYTHON"
# P  Y  T  H  O  N
# 0  1  2  3  4  5  (Positive)
# -6 -5 -4 -3 -2 -1 (Negative)

print(s[0])  # P
print(s[-1]) # N
```

### ⚠️ IndexError
Accessing an index that doesn't exist raises `IndexError`.
```python
l = [1, 2]
print(l[5]) # IndexError: list index out of range
```
