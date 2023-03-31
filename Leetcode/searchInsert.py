"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
def searchInsert(nums, target):
    i = 0
    put = 0
    found = False
    while i < len(nums)-1 and found == False:
        if nums[i] < target and nums[i+1] >= target:
            put = i + 1
            found = True 
        i += 1
    if nums[-1] < target:
        put = len(nums)
    print(put)
    return put

searchInsert([1,3,5,6],7)