# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.
# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.

# https://leetcode.com/problems/relative-ranks/description/

# 1) efficient approach using dictionary and list
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        # reverse sort the input list
        ranked_nums = sorted(nums, reverse=True)

        # init the list to store the result
        result = []
        # init the dictionary to store value-index pair
        index_dict = {}
        # list for the top-3
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        # iterate to build the dictionary
        for i in range(0,min(len(nums),3)):
            index_dict[ranked_nums[i]] = medals[i]

        for j in range(3, len(ranked_nums)):
            index_dict[ranked_nums[j]] = str(j+1)

        # iterate the original input list to retrive index from the dictionary
        for num in nums:
            result.append(index_dict[num])

        return result

# 2) inefficient approach using list only
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranked_nums = sorted(nums, reverse=True)
        result = []
        for num in nums:
            if(ranked_nums.index(num) == 0):
                result.append("Gold Medal")
            elif(ranked_nums.index(num) == 1):
                result.append("Silver Medal")
            elif(ranked_nums.index(num)==2):
                result.append("Bronze Medal")
            else:
                result.append(str(ranked_nums.index(num)+1))
        return(result)

