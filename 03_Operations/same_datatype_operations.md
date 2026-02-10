# Same Datatype Operations

Operations behave differently depending on the data type.

## 1. String + String (Concatenation)
Using `+` between strings joins them.
```python
"Hello" + "World" # "HelloWorld"
```

## 2. List + List (Concatenation)
Using `+` between lists merges them.
```python
[1, 2] + [3, 4] # [1, 2, 3, 4]
```

## 3. Tuple + Tuple
Similar to lists, tuples can be merged.
```python
(1, 2) + (3, 4) # (1, 2, 3, 4)
```

## 4. Set - Set (Difference)
Sets support mathematical difference. *They do NOT support `+`*.
```python
{1, 2, 3} - {3} # {1, 2}
```
*Note: `{1} + {2}` causes an Error.*
