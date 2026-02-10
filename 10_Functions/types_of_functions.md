# Types of User-Defined Functions

Functions can be classified based on arguments and return values.

## 1. No Arguments, No Return
Do something simple, send nothing back.
```python
def greet():
    print("Hello")
```

## 2. With Arguments, No Return
Takes input, processes it, prints/modifies something.
```python
def greet(name):
    print(f"Hello {name}")
```

## 3. With Arguments, With Return
Takes input, processes it, returns a result. **(Most Common)**
```python
def add(a, b):
    return a + b
```
