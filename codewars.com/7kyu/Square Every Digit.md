Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

# Solution

```
def square_digits(num):
    return int(''.join(map(str, (map(lambda x: pow(int(x), 2), list(str(num)))))))
```
___
# Other Solutions
```
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
```
