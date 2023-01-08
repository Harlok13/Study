Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

# Solution

```
def find_short(s):
    return len(min(s.split(), key=len))
```
