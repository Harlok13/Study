"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]
"""



def two_sum(nums, target: int):
    # res = [i for i in nums if i <= target]
    d = {}
    for k, v in enumerate(nums):

        if not d:
            d.update({abs(target - v): k})
        else:
            if v not in d:
                d.update({target - v: k})
            else:

                return [d.get(v), k]



print(two_sum([0,3,-3,4,-1], -1))
