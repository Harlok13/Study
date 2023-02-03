Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

**For example:**
```
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
```

# Solution
```python
def unique_in_order(sequence):
    last, res_lst = None, []
    for item in sequence:
        if item != last:
            res_lst.append(item)
            last = item
    return res_lst
```
___
___
# Other Solutions
```python
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
```
___
```python
def unique_in_order(iterable):
    return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]
```
