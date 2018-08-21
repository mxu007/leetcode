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

# https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        length = len(nums)
        # if only three elements, directly return results
        if length == 3:
            return nums[0]*nums[1]*nums[2]
        # sort the input list
        nums = sorted(nums)
        # two cases to get the largest products: two negatives one positive and three positive
        # return whatever is larger
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
