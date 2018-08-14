# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:

# Input: 38
# Output: 2
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
#              Since 2 has only one digit, return it.
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

# https://leetcode.com/problems/add-digits/description/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        # e.g. 0 --> 0; 18 % 9 = 0, 18 --> 9; 19 % 9 = 1 19 --> 1
        return (num if num == 0 else (9 if num % 9 == 0 else num % 9))

        if num == 0:
            return 0
        else:
            return (num % 9 if num % 9 != 0 else 9)
