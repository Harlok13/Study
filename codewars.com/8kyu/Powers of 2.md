Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

**Examples**
```
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
```

# Solution
```python
def powers_of_two(n):
    if n == 0:
        return [1]
    p = [2 ** n]

    return sorted(p + powers_of_two(n-1))
```
```python
def powers_of_two(n):
    return [n ** i if i > 0 else 1 for i in range(n+1)]
```
