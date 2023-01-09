This time we want to write calculations using functions and get the results. Let's have a look at some examples:
```
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
```
**Requirements:**

- There must be a function for each number from 0 ("zero") to 9 ("nine")
- There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
- Each calculation consist of exactly one operation and two numbers
- The most outer function represents the left operand, the most inner function represents the right operand
- Division should be integer division. For example, this should return 2, not 2.666666...:

`eight(divided_by(three()))`

# Solution

```
def calculate_expression(func):
    operands = {'plus': '+', 'minus': '-', 'times': '*', 'divided_by': '/'}

    def wrapper(operand=None):
        if operand is not None:
            expression = operands.get(operand.split()[0]) + operand.split()[1]
            if expression.startswith('/'):
                return int(eval(f'{func()} {expression}'))
            else:
                return eval(f'{func()} {expression}')

        return func()

    return wrapper


plus = lambda var: f'plus {var}'
minus = lambda var: f'minus {var}'
times = lambda var: f'times {var}'
divided_by = lambda var: f'divided_by {var}'


@calculate_expression
def zero(operand=None):
    return 0


@calculate_expression
def one(operand=None):
    return 1


@calculate_expression
def two(operand=None):
    return 2


@calculate_expression
def three(operand=None):
    return 3


@calculate_expression
def four(operand=None):
    return 4


@calculate_expression
def five(operand=None):
    return 5


@calculate_expression
def six(operand=None):
    return 6


@calculate_expression
def seven(operand=None):
    return 7


@calculate_expression
def eight(operand=None):
    return 8


@calculate_expression
def nine(operand=None):
    return 9


if __name__ == '__main__':
    print(zero(plus(six())))
    print(five(divided_by(two())))
    print(nine(times(zero())))
    print(eight(plus(seven())))

    assert zero(plus(six())) == 6, f'{zero(plus(six()))}'
    assert five(divided_by(two())) == 2, f'{five(divided_by(two()))}'
    assert nine(times(zero())) == 0, f'{nine(times(zero()))}'
    assert eight(plus(seven())) == 15, f'{eight(plus(seven()))}'
```
