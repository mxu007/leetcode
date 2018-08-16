# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

# Note:

# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# Example:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # less than two numbers in the input list
        if len(numbers) < 2:
            return False

        # init the complement dictionary, the complement of a number is the target value subtracted by this number
        # this dictionary has complement_value-number_position pair
        complement_dict = {}
        # iterate thru the input list
        for i in range(len(numbers)):
            # if find the number currently iterated is the complement of another number
            # retrieve the index of the complement and current index
            if numbers[i] in complement_dict:
                # have to return the complement first as it has a lower value (the input list is sorted)
                return [complement_dict[numbers[i]]+1, i+1]
            # add the complement_value-number position pair to the dictionary
            else:
                complement_dict[target - numbers[i]] = i

        return False
