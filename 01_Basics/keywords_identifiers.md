# Keywords and Identifiers

## 🔑 Keywords
Keywords are **reserved words** in Python. They have special meanings designated by the language syntax.
**You cannot use keywords as variable names, function names, or any other identifiers.**

### Common Keywords:
-   `False`, `True`, `None`
-   `and`, `or`, `not`
-   `if`, `elif`, `else`
-   `for`, `while`, `break`, `continue`
-   `def`, `return`, `class`
-   `try`, `except`, `finally`

*Note: All keywords in Python are case-sensitive.*

## 🏷️ Identifiers
An **identifier** is a name used to identify a variable, function, class, module, or other object.

### Rules for Identifiers
1.  **Must not be a keyword:** (e.g., `if`, `for`, `class` cannot be identifiers).
2.  **No spaces allowed:** Use underscores (`_`) instead (e.g., `my_variable`).
3.  **Must not start with a number:** Can contain numbers after the first character (e.g., `value1` is valid, `1value` is invalid).
4.  **Only `_` (underscore) allowed as a special character:** No `@`, `#`, `$`, `%`, etc.
5.  **Case-sensitive:** `Name` and `name` are treated as different identifiers.
6.  **Can be alphanumeric:** Can contain letters (a-z, A-Z) and numbers (0-9).
7.  **Maximum length:** While there's no strict limit enforced by Python, PEP 8 (Python's style guide) recommends keeping lines under 79 characters, which implicitly suggests keeping identifiers reasonably short and descriptive.
    *   **Valid:** `total_marks`, `_private_var`, `myFunction1`, `MAX_VALUE`
    *   **Invalid:** `2value`, `my value`, `my-variable`, `class` (keyword)

### Trick (Naming Conventions - PEP 8):
*   **Variables and functions:** `lowercase_with_underscores` (snake_case).
*   **Constants:** `UPPERCASE_WITH_UNDERSCORES`.
*   **Classes:** `CamelCase` (PascalCase).
*   **Private members (by convention):** Start with a single underscore `_private_method`.
*   **Name mangling (for truly private-like attributes):** Start with double underscores `__mangled_attribute`.
1.  **Variables & Functions**: Use `snake_case` (e.g., `my_variable`, `calculate_sum`).
2.  **Classes**: Use `PascalCase` (e.g., `MyClass`, `StudentData`).
3.  **Constants**: Use `UPPER_CASE` (e.g., `PI`, `MAX_VALUE`).

---

### 🧠 Interview Point: Total Keywords
**Q: How many keywords are there in Python?**
**A:** Around 35 (in Python 3.x).
You can check them programmatically:
```python
import keyword
print(keyword.kwlist)
```
