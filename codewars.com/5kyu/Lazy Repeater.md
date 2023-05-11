makeLooper()The function (make_looper in Python) takes a string
(of non-zero length) as an argument. It returns a function. The 
function it returns will return successive characters of the string
on successive invocations. It will start back at the beginning of
the string once it reaches the end.

**For example:**
```
abc = make_looper('abc')
abc() # should return 'a' on this first call
abc() # should return 'b' on this second call
abc() # should return 'c' on this third call
abc() # should return 'a' again on this fourth call
```

# Solution
```python
def make_looper(string):
    index = 0
    def looper():
        nonlocal index
        if index == len(string):
            index = 0
        result = string[index]
        index += 1
        return result
    return looper

# another sol
from itertools import cycle

class make_looper(cycle):
    def __call__(self):
        return self.__next__()
```