You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

**Examples:(Input --> Output)**
```
121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
```

# Solution

```python
def find_next_square(sq):
    return int(pow(sq ** .5 + 1, 2)) if sq ** .5 == int(sq ** .5) else -1
```
___
# Other Solutions
```python
def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2
```
___
```python
import math


def find_next_square(sq):
    return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1
```
