# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# https://leetcode.com/problems/plus-one/description/

# 1) iteartive reversely, O(n) time complexity
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if (len(digits)==0): return 1

        carry = 1
        for i in reversed(range(len(digits))):
            if digits[i] + carry >= 10:
                digits[i] = (digits[i] + carry) % 10
                carry = 1
                if i == 0: digits = [1] + digits
            else:
                digits[i] = digits[i] + carry
                return digits
        return digits


# 2) convert to numbers then plus 1 then convert back to list of integers
class Solution(object):
    def plusOne(self,digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]
