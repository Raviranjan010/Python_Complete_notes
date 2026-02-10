# Python `input()` and `eval()`

This guide explains how **`input()`**, **string concatenation**, **`type()`**, and **`eval()`** work in Python, with clear examples and outputs.

---

## 📌 1. Taking User Input Using `input()`

```python
a = input("Enter your name\n")
```

### 🔍 Explanation

- `input()` pauses the program and waits for the user to type something.
- The text inside quotes is called a **prompt**.
- `\n` creates a new line.
- The entered value is stored in variable `a`.

⚠️ **Important Rule (Python 3)**  
`input()` always returns a string (`str`).

---

## 📌 2. Printing Output Using String Concatenation

```python
print("Hello, " + a + "!")
```

### 🔍 Explanation

- `+` is used to join strings (string concatenation).
- Combines greeting text with user input.

### 🧪 Example Output

```
Enter your name
Ravi
Hello, Ravi!
```

---

## 📌 3. Checking Data Type Using `type()`

```python
type(a)
```

### ✅ Output

```python
<class 'str'>
```

---

## 📌 4. Using `eval()` to Evaluate Expressions

```python
user_input = input("Enter a math problem: ")
calculated_value = eval(user_input)
print(calculated_value)
```

### 🧪 Example

```
Enter a math problem: 5 + 5
10
```

---

## 📌 5. Using `eval()` to Accept Numeric Input

```python
b = eval(input("Enter Your age: \n"))
print("Your age is", b)
type(b)
```

### 🧪 Example Output

```
Enter Your age:
21
Your age is 21
```

```python
<class 'int'>
```

---

## ⚠️ Warning About `eval()`

`eval()` executes any Python code and can be dangerous.

### ✅ Safer Alternatives

```python
int(input())
float(input())
```

---

## 🧠 Summary

| Function | Purpose |
|--------|--------|
| `input()` | Takes user input (string) |
| `print()` | Displays output |
| `type()` | Shows data type |
| `eval()` | Evaluates expressions |

---

## ✅ Best Practices

- Prefer `int()` or `float()` over `eval()`
- Always validate user input
- Avoid executing unknown expressions

---
