**DESCRIPTION:**

Find the missing letter\
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.\
The array will always contain letters in only one case.

**Example:**
```
['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
```
(Use the English alphabet with 26 letters!)

# Solution
```python
def find_missing_letter(chars):
    d = {}
    for i in chars:
        d.update({ord(i): i})
    for j in range(min(d), max(d)):
        if j in d.keys():
            continue
        else:
            return chr(j)
```
___
# Other Solutions
```python
def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))
```
```python
def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))
```
```python
def find_missing_letter(chars):
    return [chr(n) for n in range(ord(chars[0]),ord(chars[-1])+1) if n not in [ord(c) for c in chars]][0]
```
```python
def find_missing_letter(chars):
    return set(chr(i) for i in range(ord(chars[0]), ord(chars[-1]) + 1)).difference(set(chars)).pop()
```
