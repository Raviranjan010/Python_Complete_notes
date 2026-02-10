# Different Datatype Operations

## 1. String * Integer (Repetition)
You can multiply a string by an integer to repeat it.
```python
"Hi" * 3 # "HiHiHi"
```

## 2. List * Integer (Repetition)
Similarly for lists.
```python
[1, 2] * 2 # [1, 2, 1, 2]
```

## ⚠️ Invalid Operations (Edge Cases)

### String + Integer
**ERROR**: `TypeError`
```python
"Age: " + 25 # TypeError: can only concatenate str (not "int") to str
```
**Fix**: `"Age: " + str(25)`

### List + Tuple
**ERROR**: `TypeError`
```python
[1, 2] + (3, 4) # TypeError
```
**Fix**: `[1, 2] + list((3, 4))`

---

### 🧠 Interview Point: Why specific types?
Python is **Strongly Typed**. It won't implicitly convert types if ambiguity exists (like Adding a number to a string). You must convert explicitely.
