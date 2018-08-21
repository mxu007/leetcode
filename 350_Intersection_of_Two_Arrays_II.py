# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:

# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/


# 1) use python collection.Counters, elegant solution
import collections
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # https://docs.python.org/3/library/collections.html
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())

# 2) given input lists are sorted
class Solution(object):
    def intersect(self, nums1, nums2):

        # sort input lists
        nums1, nums2 = sorted(nums1), sorted(nums2)

        # init pointers and result list
        pt1 = pt2 = 0
        result = []

        while True:
            try:
                # if list 1 element is larger, move pointer at list 2
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                # if list 2 element is larger, move pointer at list 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                # two elements equal
                else:
                    result.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return result
