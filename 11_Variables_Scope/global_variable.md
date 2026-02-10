# Global Variables

A variable declared **outside** any function is a global variable.
It can be accessed by any function.

```python
x = 10 # Global

def my_func():
    print(x) # Accesses Global x

my_func()
```

## The `global` Keyword
If you want to **modify** a global variable inside a function, you MUST use the `global` keyword.
Otherwise, Python will create a new local variable with the same name.

```python
count = 0

def increment():
    global count # Tell Python we mean the global 'count'
    count += 1
```
