# Python String Methods Reference

Common built-in methods for string manipulation.

## Case Conversion
| Method | Description | Example |
| :--- | :--- | :--- |
| `.upper()` | Converts to uppercase | `"hi".upper()` -> `"HI"` |
| `.lower()` | Converts to lowercase | `"HI".lower()` -> `"hi"` |
| `.swapcase()` | Swaps case | `"Hi".swapcase()` -> `"hI"` |
| `.capitalize()` | Capitalizes first letter | `"hello".capitalize()` -> `"Hello"` |
| `.title()` | Capitalizes first letter of every word | `"hello world".title()` -> `"Hello World"` |

## Checks (Boolean)
| Method | Description | Example |
| :--- | :--- | :--- |
| `.isupper()` | Checks if all chars are uppercase | `"A".isupper()` -> `True` |
| `.islower()` | Checks if all chars are lowercase | `"a".islower()` -> `True` |
| `.isalpha()` | Checks if all chars are alphabets | `"abc".isalpha()` -> `True` |
| `.isdigit()` | Checks if all chars are digits | `"123".isdigit()` -> `True` |
| `.isalnum()` | Checks if alphanumeric (letters + nums) | `"a1".isalnum()` -> `True` |

## Splitting and Joining
| Method | Description | Example |
| :--- | :--- | :--- |
| `.split(sep)` | Splits string into a **List** | `"a,b".split(",")` -> `['a', 'b']` |
| `.join(iter)` | Joins an iterable into a **String** | `"-".join(['a', 'b'])` -> `"a-b"` |

## Trimming (Whitespace Removal)
| Method | Description | Example |
| :--- | :--- | :--- |
| `.strip()` | Removes leading & trailing whitespace | `"  hi  ".strip()` -> `"hi"` |
| `.lstrip()` | Removes left (leading) whitespace | `"  hi".lstrip()` -> `"hi"` |
| `.rstrip()` | Removes right (trailing) whitespace | `"hi  ".rstrip()` -> `"hi"` |

## Search and Replace
| Method | Description | Example |
| :--- | :--- | :--- |
| `.count(sub)` | Counts occurrences of substring | `"banana".count("a")` -> `3` |
| `.find(sub)` | Returns **first index** of substring (or -1) | `"hello".find("e")` -> `1` |
| `.rfind(sub)` | Returns **last index** of substring | `"hello".rfind("l")` -> `3` |
| `.index(sub)` | Like find() but raises Error if not found | `"hello".index("z")` -> `ValueError` |
| `.replace(old, new)` | Replaces substring | `"hi".replace("i", "ey")` -> `"hey"` |
| `.startswith(sub)` | Checks if starts with substring | `"hi".startswith("h")` -> `True` |
| `.endswith(sub)` | Checks if ends with substring | `"hi".endswith("i")` -> `True` |
