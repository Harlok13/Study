Complete the solution so that it strips all text that follows
any of a set of comment markers passed in. Any whitespace at
the end of the line should also be stripped out.

**Example:**

**Given an input string of:**
```
apples, pears # and bananas
grapes
bananas !apples
```
**The output expected would be:**
```
apples, pears
grapes
bananas
```
**The code would be called like so:**
```
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
```

# Solution

```python
def strip_comments(strng, markers=None):
    sentences = strng.split('\n')
    for marker in markers:
        sentences = [sentence.split(marker)[0].rstrip() for sentence in sentences]
    return '\n'.join(sentences)
```
___
___
# OtherSolutions
```python
solution=lambda t,m,r=__import__('re'):r.sub(r'( *[{}].*)'.format(r.escape(''.join(m))),'',t)if m else t
```
___
```python
import re
def solution(string, markers):
    return string if not markers else re.sub(f" *[{re.escape(''.join(markers))}].*", "", string, re.MULTILINE)
```
___
```python
def strip_comments(strng, markers):
    for num, marker in enumerate(markers):
        strng = '\n'.join([i.split(marker)[0].rstrip() for i in strng.split('\n')])

    return strng
```
