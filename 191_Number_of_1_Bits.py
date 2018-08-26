# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Example 1:

# Input: 11
# Output: 3
# Explanation: Integer 11 has binary representation 00000000000000000000000000001011
# Example 2:

# Input: 128
# Output: 1
# Explanation: Integer 128 has binary representation 00000000000000000000000010000000

# https://leetcode.com/problems/number-of-1-bits/description/

# 1) convert to binary string and then sum individual bits
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_bin = "{0:b}".format(n)
        return sum(int(i) for i in n_bin)

# 2) built in bin function
class Solution(object):
    def hammingWeight(self, n):
         return bin(n).count('1')

# 3) bit operations
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            # n & operation with n-1 will cancel the left most available bit, so c gets updated by 1
            n &= n - 1
            c += 1
        return c
