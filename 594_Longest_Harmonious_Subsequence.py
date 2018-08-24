# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.

# https://leetcode.com/problems/longest-harmonious-subsequence/description/

# 1) Improved version of using dictionary
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dict to capture occurence of numbers
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        # check if current key + 1 exist in dict
        possible_len = ([count[key]+count[key+1] for key in count.keys() if key+1 in count])
        return max(possible_len) if len(possible_len) > 0 else 0

# 2) Time complexity not optimized
import itertools
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dict to capture occurence of numbers
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        # create combination where max and min with exactly one diffrence
        keys = list(count.keys())
        combinations = [[i,j] for i in keys for j in keys if (j-i)==1]
        print(combinations)
        result = 0

        # iterate possible combinations
        for combination in combinations:
            length = count[combination[0]] + count[combination[1]]
            if result < length:
                result = length

        return result

# 3) Smart way to iterate the list, update dictionary and get the result
# https://leetcode.com/problems/longest-harmonious-subsequence/solution/
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dict to capture occurence of numbers
        count = {}
        result = 0
        for num in nums:
            count[num] = count.get(num,0) + 1
            if num + 1 in count:
                result = max(result, count[num]+count[num+1])
            if num - 1 in count:
                result = max(result, count[num]+count[num-1])

        return result

