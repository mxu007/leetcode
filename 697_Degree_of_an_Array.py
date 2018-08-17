# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6

# https://leetcode.com/problems/degree-of-an-array/description/

# 1) more efficient appraoch using list
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # init the dictioanry to store number-occurence pair
        num_count = {}

        # iterate input list to build the dictionary
        for num in nums:
            num_count[num] = num_count.get(num,0)+1

        # get the highest number of occurences
        highest = max(num_count.values())
        # get the numbers with most frequent occurences in the original list
        max_nums = [k for k,v in num_count.items() if v == highest]

        # store the smallest possible length of subarray whih has the same degree
        # as multiple numbers can have the same number of occurences, use list here
        shortest_lens = []
        for max_num in max_nums:
            # find the distance between first and last index of the value in the list
            shortest_lens.append(len(nums) - nums[::-1].index(max_num) - nums.index(max_num))

        # return the smallest possible length
        return min(shortest_lens)

# slower version using multi for loops
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num,0)+1

        highest = max(num_count.values())
        max_nums = [k for k,v in num_count.items() if v == highest]
        print(num_count, max_nums)

        shortest_len = 10 ** 20

        for max_num in max_nums:
            max_indices = [i for i, val in enumerate(nums) if val == max_num]
            if (max_indices[-1]-max_indices[0]+1< shortest_len):
                shortest_len = max_indices[-1]-max_indices[0]+1

        return shortest_len
