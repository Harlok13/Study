You are given a binary tree:
```python
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
```
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:
```
                 2
            8        9
          1  3     4   5
```
Should return following list:
```
[2,8,9,1,3,4,5]
```
Example 2 - following tree:
```
                 1
            8        4
              3        5
                         7
```
Should return following list:
```
[1,8,4,3,5,7]
```

# Solution
```python
def tree_by_levels(node: object) -> list:
    """Sort binary tree by levels."""
    nodes, result = [node], []
    while nodes:
        if (vertex := nodes.pop(0)) is not None:
            result.append(vertex.value)
            nodes += [vertex.left, vertex.right]
    return result
```
