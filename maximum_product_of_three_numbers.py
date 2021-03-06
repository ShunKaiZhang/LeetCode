# python3
# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:
# Input: [1,2,3]
# Output: 6
# Example 2:
# Input: [1,2,3,4]
# Output: 24
# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


# My solution
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0]*nums[1]
        nums.sort()
        if nums[0] < 0 and nums[1] < 0 and nums[0]*nums[1] > nums[len(nums)-2]*nums[len(nums)-3]:
            return nums[0]*nums[1]*nums[len(nums)-1]
        else:
            return nums[len(nums)-2]*nums[len(nums)-3]*nums[len(nums)-1]