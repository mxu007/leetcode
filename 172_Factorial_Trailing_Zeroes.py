# Given an integer n, return the number of trailing zeroes in n!.

# Example 1:

# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Note: Your solution should be in logarithmic time complexity.

# https://leetcode.com/problems/factorial-trailing-zeroes/description/

# 1) 2 is easy to get, so count how many factor of 5 we have
# 25 has 2 factor of 5, 125 has 3 factor of 5
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 5
        while (n/i>=1):
            count += int(n/i)
            i *= 5

        return count

# 2) recursive approach
# https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52367/My-explanation-of-the-Log(n)-solution
import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n/5 + self.trailingZeroes(n/5)
