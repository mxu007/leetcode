# In a given integer array nums, there is always exactly one largest element.

# Find whether the largest element in the array is at least twice as much as every other number in the array.

# If it is, return the index of the largest element, otherwise return -1.

# Example 1:

# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


# Example 2:

# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


# Note:

# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99].

# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

# 1) iterate the list to find largest and use sort to find the 2nd largest
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        index = 0
        large = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > large:
                large = nums[i]
                index = i
        sorted_nums = sorted(nums)
        sorted_nums.pop()
        return index if large >= 2*sorted_nums[-1] else -1

# 2) just use the list sort to find the largest and 2nd largest item, O(nlogn) time
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return 0
        sorted_nums = sorted(nums)
        return nums.index(sorted_nums[-1]) if sorted_nums[-1] >= 2*sorted_nums[-2] else -1


# 3) two variable to store highest and second highest, O(n) time
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return -1

        highest = -1
        secondHighest = -1
        highestIndex = 0

        for i,n in enumerate(nums):
            if n >= highest:
                secondHighest = highest
                highest = n
                highestIndex = i
            elif n > secondHighest:
                secondHighest = n

        if highest < secondHighest*2:
            highestIndex = -1

        return highestIndex
