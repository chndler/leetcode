"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum(nums, target):
    """
    brute-force, O(n^2)
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    j = 1
    while True:
        print(i, j)
        if nums[i] + nums[j] == target:
            return [i, j]
        if j < len(nums)-1:
            j+=1
        else:
            i+=1
            j=i+1
            
def twoSumMap(nums, target):
    """
    hash map, O(n)
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    prevMap = {}
    
    for i, n in enumerate(nums):
        diff = target - n
        print(i, n, ":", diff, prevMap)
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
            
