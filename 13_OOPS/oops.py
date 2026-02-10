# ---------------------------------------------------------
# Topic: OOP (Class, Object, Inheritance, Encapsulation)
# File: oops.py
# ---------------------------------------------------------

# --- 1. Class and Constructor ---
class Dog:
    # Class Attribute (Shared by all dogs)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance Attributes (Unique to each dog)
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

# Creating Objects
buddy = Dog("Buddy", 3)
miles = Dog("Miles", 5)

print(f"{buddy.name} is {buddy.age} years old.")
print(buddy.bark())

# --- 2. Inheritance ---
class ElectricCar(Dog): # Bad example logically, but shows syntax
    pass

# Better Example
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak() # Meow

# --- 3. Encapsulation (Private Members) ---
class Account:
    def __init__(self):
        self.__balance = 1000 # Private

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}")

    def show_balance(self):
        # Can access private var inside the class
        print(f"Balance: {self.__balance}")

acc = Account()
acc.deposit(500)
acc.show_balance()
# print(acc.__balance) # Error: AttributeError
