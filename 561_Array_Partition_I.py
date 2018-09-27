# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

# Example 1:
# Input: [1,4,3,2]

# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].

# https://leetcode.com/problems/array-partition-i/description/

# 1) sort the array, O(Nlog(N)) time for sorting
# grouping is from left to the right
# e.g. 1,3,2,4 could be grouped as [1,3], [2,4], which gives 1 + 2 = 3
# it could also be grouped as [1,2], [3,4] which gives 1 + 3 = 4
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for i in range(0,len(nums)-1,2):
            sum += nums[i]
        return sum

# 2) one-liner
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([num for i,num in enumerate (sorted(nums)) if i % 2 ==0 ])

# 3) further simplified one-liner
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

# 4) hashing solution using counting sort
# https://www.geeksforgeeks.org/counting-sort/
# The sorting is achieved on counting occurence of numbers and more importantly we traverse from smallest number index to the largest
# the adjust flag is to pair number with odd number of occurence to its nearest next neighbor
# e.g. [1,1,2,3,4,4], the freq for 2 is odd, trigger the adjust set to True.
# Hence when we move to 3, as it needs to be paired with 2 and won't be added to total sum due to the min of the pair requirement.
# The freq for 3 is reduced by 1 in freq = freq-1 if adjust else freq and 3 is not added to s_so_far.
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0]*20001
        for x in nums:
            res[x+10000] += 1
        s_so_far, adjust = 0, False
        for idx, freq in enumerate(res):
            if freq:
                freq = freq-1 if adjust else freq
                if freq&1:
                    s_so_far += ((freq//2) + 1)*(idx-10000)
                    adjust = True
                else:
                    s_so_far += ((freq//2))*(idx-10000)
                    adjust = False
        return s_so_far
