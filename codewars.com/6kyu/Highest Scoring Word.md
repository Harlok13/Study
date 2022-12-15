**DESCRIPTION:**

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

# Solution

```
def high(x):
    d = {}
    for i in x.lower().split():
        lst = []
        for j in i:
            lst.append(ord(j) - 96)
        if lst:
            if sum(lst) not in d:
                d.update({sum(lst): i})
                lst.clear()
            else:
                lst.clear()
    m = max(d)

    return d.get(m, None)
```
___
# Other Solutions
```
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
```
