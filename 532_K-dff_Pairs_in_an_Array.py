# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# Note:
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].

# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

# 1) use itertools, exceed memory limit, O(N^2) space due to combination
import itertools
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k: nums = list(set(nums))
        comb = list(itertools.combinations(nums, 2))
        return len(set([(i[0],i[1]) for i in comb if abs(i[0]-i[1])== k]))


# 2) use dictionary, O(N) to create the dictionary and iterate nums, O(1) to perform a search
# overall O(N) time and O(N) space
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or len(nums)==0: return 0

        count_dict = {}
        count = 0
        for num in nums:
            count_dict[num] = count_dict.get(num,0) + 1

        for key in count_dict:
            if k:
                if key + k in count_dict: count += 1
            else:
                if count_dict[key] > 1: count += 1
        return count

# 3) variant of 2 using collections.Counter which returns a counter dictionary
import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        count_dict = collections.Counter(nums)
        for i in count_dict:
            if k > 0 and i + k in count_dict or k == 0 and count_dict[i] > 1:
                count += 1
        return count


# 4) two pointers with input nums sorted. i is the lower index, j is the higher index
# sort takes O(Nlog(N)).
# for loop takes O(N) only because the limit of  nums[j] - nums[i] < k and nums[i] == nums[i+1]
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i, j, count = 0, 0, 0
        nums.sort()
        while i < len(nums):
            j = max(j,i+1)
            while j < len(nums) and nums[j] - nums[i] < k:
                j += 1
            if j < len(nums) and nums[j] - nums[i] == k:
                count += 1
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return count

# 5) variant of 4)
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if (k < 0): return 0
        i, j, count = 0, 1, 0
        nums.sort()
        while j < len(nums):
            if j<=i or nums[i]+k > nums[j]:
                j += 1
            elif (i > 0 and nums[i] == nums[i-1]) or (nums[i] + k < nums[j]):
                i += 1
            # handle case nums[i] + k == nums[j]
            else:
                count += 1
                i += 1
        return count

# 6) use AND operation between two sets and collections.Counter
import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > 0:
            return len(set(nums)&set(n+k for n in nums))
        elif k == 0:
            sum(v > 1 for v in collections.Counter(nums).values())
        else:
            return 0
