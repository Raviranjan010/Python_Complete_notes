# Polymorphism

**Poly** (Many) + **Morp** (Forms).
It refers to methods having the same name but performing different actions.

## 1. Method Overriding (Run-time Polymorphism)
If a Child class has a method with the same name as the Parent class, the Child's method **overrides** the Parent's.

```python
class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def speak(self):
        print("Bark") # Overrides

d = Dog()
d.speak() # Bark
```

## 2. Duck Typing (Python Special)
"If it looks like a duck and quacks like a duck, it's a duck."
Python doesn't care about the type of object, only if it has the method we are calling.
