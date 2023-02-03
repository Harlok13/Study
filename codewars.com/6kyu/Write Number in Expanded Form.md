**Write Number in Expanded Form**

You will be given a number and you will need to return it as a string in Expanded Form. For example:
```
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
```
NOTE: All numbers will be whole numbers greater than 0.

# Solution

```python
def expanded_form(num):
    lst = reversed(list(str(num)))
    fil = filter(lambda x: x != '0', [str(int(v) * (1, 10 ** k)[k>0]) for k, v in enumerate(lst)])
    return ' + '.join(reversed(list(fil)))
```
