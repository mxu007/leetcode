# Given an integer, write a function to determine if it is a power of three.

# Example 1:

# Input: 27
# Output: true
# Example 2:

# Input: 0
# Output: false
# Example 3:

# Input: 9
# Output: true
# Example 4:

# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?

# https://leetcode.com/problems/power-of-three/description/

# 1) recursive approach
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n == 0:
            return False

        if n % 3 != 0:
            return False
        else:
            return self.isPowerOfThree(n/3)


# 2) iterative approach
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n == 0:
            return False

        while(n!=1):
            if(n%3!=0):
                return False
            else:
                n=n/3
        return True

# 3) one line
class Solution:
    def isPowerOfThree(self, n):
        # A remainder of 0 means n is a divisor of 3^{19} and therefore a power of three.
        return n>0 and 1162261467 % n == 0

