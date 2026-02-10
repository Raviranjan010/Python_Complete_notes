# Encapsulation

Encapsulation is wrapping code and data together.
It is also about **hiding** sensitive data.

## Access Modifiers
Python doesn't have strict `private` or `public` keywords like Java, but uses **conventions**.

### 1. Public
Accessible everywhere.
`self.name`

### 2. Protected
Intended for internal use (or subclasses). Prefix with `_`.
`self._name`

### 3. Private
Not accessible from outside the class. Prefix with `__` (double underscore).
`self.__name`
*Python performs name mangling to make it harder to access.*

```python
class Bank:
    def __init__(self):
        self.__balance = 100 # Private
    
b = Bank()
# print(b.__balance) # AttributeError
```
