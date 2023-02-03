**DESCRIPTION:**

You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

**Examples**
```
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
```

# Solution

```python
def stray(arr):
    res = __import__('collections').Counter(arr)
    a = [k for k, v in res.items() if v == 1]
    return a[0]
```
___
# Other Solutions

```python
def stray(arr):
    return min(arr, key=arr.count)
```
