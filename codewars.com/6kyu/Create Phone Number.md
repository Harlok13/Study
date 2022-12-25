**DESCRIPTION:**

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

**Example**
```create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"```
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

# Solution

```
def create_phone_number(n):
    k = list(map(str, n))
    return f'({"".join(k[:3])}) {"".join(k[3:6])}-{"".join(k[6:])}'
```
___
# Other Solutions

```
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
```
