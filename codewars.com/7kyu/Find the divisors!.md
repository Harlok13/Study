Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

**Example:**
```
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
```

# Solution

```
def divisors(integer):
    x = [i for i in range(2, integer) if not integer % i] 
    if len(x) > 0: return x
    else: return f"{integer} is prime"
```
___
# Other Solutions

```
def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n
```
