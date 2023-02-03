Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
```
[
  "  *  ",
  " *** ", 
  "*****"
]
```
And a tower with 6 floors looks like this:
```
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
```

# Solution

```python
def tower_builder(n):
    return [('*' + '*' * (2 * k)).center(n*2-1, ' ') for k, v in enumerate(range(n))]
```
enumerate  явно лишний, забыл его убрать
