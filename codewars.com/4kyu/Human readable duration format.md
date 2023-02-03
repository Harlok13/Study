**DESCRIPTION:**

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

# Solution

```python
def format_duration(sec):
    t = __import__('time').gmtime(sec)
    y, d, h, m, s = t.tm_year - 1970, t.tm_yday, t.tm_hour, t.tm_min, t.tm_sec
    
    years = (f'{y} years ', f'{y} year ')[y == 1]
    days = (f'{d - 1} days ', f'{d - 1} day ')[d == 1]
    hours = (f'{h} hours ', f'{h} hour ')[h == 1]
    minutes = (f'{m} minutes ', f'{m} minute ')[m == 1]
    seconds = (f'{s} seconds', f'{s} second')[s == 1]
    
    res = ('', years)[bool(y)] + ('', days)[bool(d-1)] + \
          ('', hours)[bool(h)] + ('', minutes)[bool(m)] + \
          ('', seconds)[bool(s)]
          
    r = [f'{v},' if k % 2 else v for k, v in enumerate(res.split())]
    if len(r) > 2:
        r[-2] = f'and {r[-2]}'
        r[-3] = r[-3].rstrip(',')
        
    return ' '.join(r).rstrip(',')
```
___
# Other Solutions
```python
times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
```
```python
def format_duration(s):
    dt = []
    for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'), (s+1, 'year')]:
        s, m = divmod(s, b)
        if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
    return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'
```
