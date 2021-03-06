# python3
# Given a list of non negative integers, arrange them such that they form the largest number.

# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.


# My solution
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = map(str, nums)
        nums.sort(cmp=lambda a, b: cmp(b + a, a + b))
        return str(int(''.join(nums)))


