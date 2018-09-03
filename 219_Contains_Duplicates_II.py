# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# https://leetcode.com/problems/contains-duplicate-ii/description/

# 1) use itertools but fails time complexity
# function duplicates return list of indices of duplicate values
import itertools
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def duplicates(lst, item):
            return [i for i,x in enumerate(lst) if x == item]

        for item in set(nums):
            if len(([comb for comb in itertools.combinations(duplicates(nums,item),2) if abs(comb[0]-comb[1]) <= k])) > 0:
                return True

        return False


# 2) use dictionary, O(N) time complexity
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2: return False
        index_dict = {}
        for i in range(len(nums)):
            if nums[i] not in index_dict:
                index_dict[nums[i]] = i
            else:
                if i - index_dict[nums[i]] <= k:
                    return True
                else:
                    index_dict[nums[i]] = i
        return False

# 3) cleanre version of using dictionary
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_dict = {}
        for i, num in enumerate(nums):
            # need to check whether num in dictionary for python 3
            if num in index_dict:
                if i - index_dict.get(num) <= k:
                    return True
            index_dict[num] = i

        return False
