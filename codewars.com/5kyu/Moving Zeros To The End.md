Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
```
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
```

# Solution

```python
def move_zeros(lst):
    res = [i for i in lst if i != 0]
    return res + [0] * (len(lst) - len(res))
```
___
# Other Solutions

```python
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
```
___
```python
def move_zeros(array):
    return [x for x in array if x] + [0]*array.count(0)
```

