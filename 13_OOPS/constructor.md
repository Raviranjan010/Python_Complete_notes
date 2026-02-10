# Constructor (`__init__`)

## 🏗️ What is a Constructor?
A special method that is **automatically called** when an object is created.
It is used to **initialize** the attributes of the object.

In Python, the constructor is named `__init__`.

## The `self` Parameter
`self` represents the **current instance of the class**.
It allows us to access variables that belong to the class.

```python
class Student:
    def __init__(self, name):
        self.name = name  # Assign argument to object's variable

s1 = Student("John")
print(s1.name) # John
```
