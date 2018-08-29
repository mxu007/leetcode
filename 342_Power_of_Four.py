# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?

# https://leetcode.com/problems/power-of-four/description/

# 1) recursive approach
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num == 0:
            return False

        if num % 4 != 0:
            return False
        else:
            return self.isPowerOfFour(num/4)

# 2) iterative approach
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num == 0:
            return False

        while(num!=1):
            if(num%4!=0):
                return False
            else:
                num=num/4
        return True

# 3) math approach
# http://www.techiedelight.com/check-given-number-power-of-4/
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and 2**31 % num == 0 and num % 3 == 1

# 4) math approach
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return not (num & (num-1)) and (num%3==1)
