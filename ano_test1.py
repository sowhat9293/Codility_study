def yourMethod(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    N = len(nums)
    # for i in range(N-1):
    #     for j in range(i+1, N):
    #         if target == nums[i] + nums[j]:
    #             return [i, j]
    d = {nums[i]:i for i in range(N)}
    for k, v in d.items():
        if v < target:
            val = target - k
            if d.get(val, None) is not None:
                return [v, d[val]]
            
    return -1
    ## Finish the given function
    ## You may test out the function as you like by running the code
    ## Please do not leave the CodePair screen unless allowed so.
    ## Good Luck

nums = [7,15,11,2]
target = 9
print(yourMethod(nums, target))



"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
