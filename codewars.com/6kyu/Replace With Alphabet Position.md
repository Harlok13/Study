**DESCRIPTION:**

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

**Example**

alphabet_position("The sunset sets at twelve o' clock.")\
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

# Solution

```python
from string import ascii_lowercase
def alphabet_position(text):
    d = {v: k for k, v in enumerate(ascii_lowercase, 1)}
    return ' '.join(map(str, [d.get(i, '') for i in text.lower() if i in d]))
```
___
# Other Solutions

```python
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
```
