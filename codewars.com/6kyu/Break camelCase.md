**DESCRIPTION:**

Complete the solution so that the function will break up camel casing, using a space between words.
```
Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```
# Solution

```python
"""
at least some ideas how to solve it...
"""
from string import ascii_uppercase as asc_up
from re import sub


def solution(s: str) -> str:
    camel = [j for j in s if j in asc_up]
    r = s
    for i in camel:
        r = sub(fr'{i}', fr' {i}', r)
    return r.replace('  ', ' ')
```
___
# Other Solutions

```python
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)
```
```python
def solution(s):
    return ''.join(i if i.islower() else ' ' + i for i in s)
```
```python
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
```
