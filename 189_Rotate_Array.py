# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Note:

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# https://leetcode.com/problems/rotate-array/description/

# 1) O(kn) time complexity where k is number of steps and n is number of elements in the input list
# O(1) extra space
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums[-1]
            for j in range(len(nums)-1,0,-1):
                nums[j] = nums[j-1]
            nums[0] = temp


# 2) improved version of # 1) using k mod length of nums to calculate the shift of index required
# extra constant space to locate [k%len(nums)] numbers
# if input list has single element, do nothing
# if k is multiple of length of input nums, do nothing
# O(n) time complexity, O(1) space
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) and len(nums) > 1:
            k = k % len(nums)
            temp = nums[-k:]
            for j in range(len(nums)-1,0,-1):
                nums[j] = nums[j-k]
            nums[0:k] = temp

# 3) single pass solution, but require O(n) space
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) and len(nums) > 1:
            k = k % len(nums)
            nums[:] = nums[-k:] + nums[:len(nums)-k]

# 4) create additional array
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) and len(nums) > 1:
            result = [None] * len(nums)
            for i in range(len(nums)):
                result[(i+k) % len(nums)] = nums[i]
            nums[:] = result

#  5) reverse list, then reverse first k%len(nums) numbers and then reverse the last n-(k%len(nums)) numbers
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) and len(nums) > 1:
            k = k % len(nums)
            nums[:] = nums[::-1]
            #print(nums[:k], nums[k:], nums[:k][::-1], nums[k:][::-1])
            nums[:k] = nums[:k][::-1]
            nums[k:] = nums[k:][::-1]


# 6) use pop and insert
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for i in range(k):
            nums.insert(0, nums.pop(-1))


