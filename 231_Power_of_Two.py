# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: 218
# Output: false

# https://leetcode.com/problems/power-of-two/description/

# 1) recursive approach
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True
        elif n == 0:
            return False

        if n % 2 != 0:
            return False
        else:
            return self.isPowerOfTwo(n/2)

# 2) iterative approach
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True
        elif n == 0:
            return False

        while(n!=1):
            if(n%2!=0):
                return False
            else:
                n=n/2
        return True
