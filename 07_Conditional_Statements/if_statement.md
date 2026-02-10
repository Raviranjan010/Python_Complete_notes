# Python Conditional Statements

This document demonstrates various ways to use conditional statements in Python, including `if`, `else`, `elif`, and nested conditions.

## 1. Check if a Number is Positive, Negative, or Zero

This example takes an integer input and checks its sign.

```python
a = int(input("Enter a number to check whether it is +ve, -ve, or 0: "))

if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("It's 0")
```

## 2. Check if a Number is Even or Odd

Uses the modulus operator `%` to determine parity.

```python
b = int(input("Enter a number to check even or odd: "))

if b % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
```

## 3. Simple Voting Eligibility Check

Checks if a person is 18 or older.

```python
c = int(input("Enter age to check voting eligibility: "))

if c >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

## 4. Calculate Average and Pass/Fail Status

Takes marks for 5 subjects, calculates the average, and determines if the student passed (Average >= 35).

```python
maths = int(input("Enter marks of Maths: "))
science = int(input("Enter marks of Science: "))
english = int(input("Enter marks of English: "))
hindi = int(input("Enter marks of Hindi: "))
social_science = int(input("Enter marks of Social Science: "))

avg = (maths + science + english + hindi + social_science) / 5
print(f"Average Marks: {avg}")

if avg >= 35:
    print("Pass")
else:
    print("Fail")
```

## 5. Day of the Week (Using `elif`)

Takes a number (1-7) and prints the corresponding day of the week.

```python
day = int(input("Enter a value (1-7) to check day: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Enter a valid number")
```

## 6. Student Result Classification (Nested `if`)

Classifies the result based on marks using nested `if-else` logic.

```python
marks = int(input("Enter obtained marks: "))

if marks >= 40:
    if marks >= 75:
        print("Result: Distinction")
    elif marks >= 60:
        print("Result: First Class")
    elif marks >= 50:
        print("Result: Second Class")
    else:
        print("Result: Pass")
else:
    print("Result: Fail")
```

## 7. Advanced Voting Eligibility (Nested `if`)

Checks eligibility based on Age, possession of a Voter ID, and status.

```python
age = int(input("Enter your age: "))

if age >= 18:
    voter_id = input("Do you have a Voter ID? (yes/no): ").lower()

    if voter_id == "yes":
        is_alive = input("Are you alive? (yes/no): ").lower()

        if is_alive == "yes":
            print("Eligible to vote")
        else:
            print("Not eligible (Person is not alive)")
    else:
        print("Not eligible (Please bring Voter ID)")
else:
    print("Not eligible (Underage)")
```

## 8. Common Exam Logic Examples

### Divisibility by 5 and 11
```python
num = int(input("Enter a num: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both")
```

### Leap Year Check
```python
year = int(input("Enter the year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It's a leap year")
else:
    print("Not a leap year")
```

## 🧠 Exam Points to Remember (Tricks & Traps)

### 1. `input()` Always Returns String
*   **Trap**: `a = input("Enter number: ")`. If user enters `5`, `a` is `"5"` (string).
*   **Fix**: Always cast to `int` or `float` for math. `a = int(input(...))`

### 2. Modulus Operator (%) Usage
*   Used for checking divisibility.
*   `num % 2 == 0` -> Even
*   `num % 10` -> Last digit of a number.

### 3. Order of Conditions (Ladder Logic)
*   When using `if-elif-else`, Python checks conditions from top to bottom.
*   **Rule**: Always check the **most specific** or **strictest** condition first.
*   **Example**: Checking for Grade A (>=90) should come before Grade B (>=80).

### 4. Short-Circuit Logic in `if`
*   `if A and B`: If A is False, B is **not evaluated**.
    *   Safe: `if x != 0 and 10/x > 1:` (Prevents ZeroDivisionError).
*   `if A or B`: If A is True, B is **not evaluated**.

### 5. Common Condition Patterns
*   **Range Check**: `if 10 <= x <= 20:` (Python supports this chaining).
*   **Empty Check**: `if not my_list:` (True if list is empty).
