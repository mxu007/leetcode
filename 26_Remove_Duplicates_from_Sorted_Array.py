# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.
# Example 2:

# Given nums = [0,0,1,1,1,2,2,3,3,4],

# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

# It doesn't matter what values are set beyond the returned length.
# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

# Internally you can think of this:

# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);

# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# This implies that if you iterate the list back to front, if you remove an item at the current index, everything to it's right shifts left - but that doesn't matter, since you've already dealt with all the elements to the right of the current position, and you're moving left - the next element to the left is unaffected by the change, and so the iterator gives you the element you expect.

# 1) use two variables prev and curr, O(N) time complexity
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = None
        for num in reversed(nums):
            curr = num
            if curr == prev:
                nums.remove(curr)
            prev = curr

        return len(nums)

# 2) use to index pointers i (slow),j (fast) to iterate the list, O(N) time complexity
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i+1

# 3) use set and sort
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(list(set(nums)))
        return len(nums)

# 4) use single index and reversely iterate, use pop
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)

