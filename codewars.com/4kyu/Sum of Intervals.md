Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ) => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ) => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ) => 19

sumIntervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ) => 100000030
Tests with large intervals
Your algorithm should be able to handle large intervals. All tested intervals are subsets of the range [-1000000000, 1000000000].

# Solution
```
def sum_of_intervals(intervals):
    res, last = 0, float('-inf')
    for a, b in sorted(intervals):
        if a > last:
            last = a
        if b > last:
            res, last = res + b - last, b
        
    return res
```
___
# Other Solutions

```
def sum_of_intervals(intervals):
   

    output = []

    # We turn our list of tuples into a list of lists
    list_of_lists = [list(x) for x in intervals]

    # We now sort the list in ascending order, according the first element in each list
    list_of_lists.sort()
    print(f" list of lists {list_of_lists}")

    # Get rid of duplicate elements
    # res will be our list without duplicates
    res = []
    [res.append(x) for x in list_of_lists if x not in res]
    print(f"res {res}")
    # We now deal with exceptions

    if len(res) < 1:
        return []
    if len(res) == 1:
        answer = res[0][1] - res[0][0]
        print(answer)
        return answer


    # Store the first interval in our list as  a variable and append it to an empty list

    interval_to_be_treated = res[0]
    output.append(interval_to_be_treated)
    # This is the clever bit. It loops through res and stores the next interval start and end values in two variables
    for i in range(len(res)):
        # We set a variable upper_limit to be the upper limit of the interval in the first element in res
        upper_limit = interval_to_be_treated[1]
        print(f"upper limit is {upper_limit}")
        # We create two variables, low_res stores the lower limit of an interval and upper_res the upper limit
        low_res = res[i][0]
        upper_res = res[i][1]
        # This is the clever bit. Check that the end value of the upper limit current2 variable is greater than or equal to the start value
        # of the next interval
        # if true, change the end value of current2 to be the max of the current end interval
        if upper_limit >= low_res:
            interval_to_be_treated[1] = max(upper_limit, upper_res)
            print(f" interval_to_be_treated[1] {interval_to_be_treated[1]}")

        else:
            # else change the value held in the current variable to be current interval in res
            interval_to_be_treated = res[i]


            output.append(interval_to_be_treated)

    print(f" output {output}")


    # We now need to iterate through output to get the lengths of the ranges
    range_value = 0
    for m in range(len(output)):
        range_value =  range_value + (output[m][1] - output[m][0])
    print(f"range value {range_value}")

    return range_value
```
