# Local Variables

A variable declared **inside** a function is a local variable.
It can **only** be accessed inside that function.

```python
def my_func():
    x = 10 # Local to my_func
    print(x)

my_func()
# print(x) # ERROR: NameError (x is not defined)
```
