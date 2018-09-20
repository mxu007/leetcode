# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].

# https://leetcode.com/problems/non-decreasing-array/description/

# 1) append 0 to the begining or list as n belongs to range [1,10000]
# if current num is greater than its next, compare the next value with previous value
# then adjust value of num accordingly to keep non-decreasing
# O(n) time, O(1) space
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 1
        nums.insert(0,-sys.maxsize-1)
        for i in range(1,len(nums)-1):
            if count < 0: return False

            if nums[i] > nums[i+1] and nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
                count -= 1
            elif nums[i] > nums[i+1] and nums[i+1] < nums[i-1]:
                nums[i+1] = nums[i]
                count -= 1

        return count >= 0

# 2) O(n) time, O(n) space
# either replace nums[i] with nums[i+1] OR replace nums[i+1] with nums[i]
class Solution():
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)


# 3) one-liner
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # zip(nums[1:], nums[:-1])): create tuples of element pair with 1 index difference. e.g. (nums[i], nums[i-1])

        # zip(nums[2:], nums[:-2])) :create tuples of element pair with 2 index difference. e.g. (nums[i], nums[i-2])

        # sum(map(lambda t: t[0] - t[1] < 0, ...) find how many time the non-decreasing rule has been violated, maximum one time violation for 1 index and 2 index difference element pair

        return sum(map(lambda t: t[0] - t[1] < 0, zip(nums[1:], nums[:-1]))) <= 1 and sum(map(lambda t: t[0] - t[1] < 0, zip(nums[2:], nums[:-2]))) <= 1
