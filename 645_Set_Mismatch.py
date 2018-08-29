# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Note:
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.

# https://leetcode.com/problems/set-mismatch/description/

# 1) not optimal time complexity
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if (len(nums)==1): return [0,1-nums[0]]

        duplicates = [x for x in nums if nums.count(x) > 1]
        duplicate = duplicates[0]
        correct = (len(nums)+1)*len(nums)/2-sum(nums)+duplicate

        return[duplicate,correct]


# 2) use set and set intersection
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==1: return [0,1-nums[0]]
        elif sum(nums) == (len(nums)+1)*len(nums)//2: return [0,0]

        missing = list(set([i for i in range(1,len(nums)+1)]) - set(nums))[0]
        return [missing+sum(nums)-(len(nums)+1)*len(nums)//2,missing]

# 3) construct a list to store count for each consecutive integers, O(N) time
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        count = [0] * (N+1)
        twice, never = 0, 0

        for x in nums:
            count[x] += 1

        for x in range(1, len(nums)+1):
            if count[x] == 2:
                twice = x
            if count[x] == 0:
                never = x
        return [twice, never]

# 4) pure math approach
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]
