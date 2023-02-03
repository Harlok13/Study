**DESCRIPTION:**

Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

**Examples(Operator, value1, value2) --> output**
```
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
```

# Solution
```python
# danger
def basic_op(operator, value1, value2): 
    return eval(f'{value1}{operator}{value2}')
```
___
# Other Solutions

```python
def basic_op(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)
```
```python
def basic_op(operator, value1, value2):
    ops = {'+': lambda a, b: a + b, 
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operator](value1, value2)
```
```python
from operator import add, div, mul, sub


def basic_op(op, a, b):
    return {'+': add, '/': div, '*': mul, '-': sub}[op](a, b)
```
```python
def basic_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2
```
