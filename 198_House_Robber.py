# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

# https://leetcode.com/problems/house-robber/description/

# 1) dynamic programming, bottom up approach
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # handle empty input, one item and two items
        length = len(nums)
        if length == 0: return 0
        elif length == 1: return nums[0]
        elif length == 2: return max(nums[0],nums[1])

        # dp bottom up approach
        dp = [None] * length
        dp[0] = nums[0]
        dp[1] = max(nums[1],dp[0])

        for i in range(2,length):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[length-1]


# 2) similar approach, directly update the input list
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # handle empty input, one item and two items
        length = len(nums)
        if length == 0: return 0

        # directly update values in input nums
        for i in range(1,len(nums)):
            if i == 1:
                nums[i] = max(nums[0],nums[1])
            else:
                nums[i] = max(nums[i-1],nums[i-2]+nums[i])

        return nums[len(nums)-1]

# 3) simplified version
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, curr = 0, 0
        for i in nums: prev,curr = curr, max(prev+i, curr)
        return curr
