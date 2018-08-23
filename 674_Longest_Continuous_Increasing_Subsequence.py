# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.

# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)==0):
            return 0

        # two variables to store current continuous subsequence length and max subsequence length
        max_len, curr_len = 1, 1

        # itearte from second to the last element
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr_len += 1
                # update max subsequence length
                max_len = max(curr_len,max_len)
            elif nums[i] <= nums[i-1]:
                curr_len = 1

        return max_len
