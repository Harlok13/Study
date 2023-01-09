**Task**

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

**Examples**
```
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
```

# Solution

```
def sort_array(source_array):
    sorted_nums = sorted(filter(lambda x: x & 1, source_array))
    k = 0
    for i in range(len(source_array)):
        if source_array[i] & 1:
            source_array[i] = sorted_nums[k]
            k += 1
            
    return source_array
```
___
# Other Solutions
```
def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]
```
___
```
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
```
