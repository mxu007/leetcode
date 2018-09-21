# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.

# https://leetcode.com/problems/hamming-distance/description/

# 1) convert integer inputs to binary string then compare character by character
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        x_bin = "{0:b}".format(x)
        y_bin = "{0:b}".format(y)

        # Use zfill function to add padding zeros to designated legnth
        if(len(x_bin)<=len(y_bin)):
            x_bin = x_bin.zfill(len(y_bin))
        else:
            y_bin = y_bin.zfill(len(x_bin))

        # Calculate hamming distance
        hamming_dist = sum(a!=b for a,b in zip(x_bin, y_bin))

        return (hamming_dist)

# 2) simplified version of 1)
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = "{:032b}".format(x)
        y_bin = "{:032b}".format(y)

        # Calculate hamming distance
        return sum(a!=b for a,b in zip(x_bin, y_bin))

# 3) further simplifcation of 2)
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum(a!=b for a,b in zip("{:032b}".format(x), "{:032b}".format(y)))


# 4) bit-wise comparison using ^ (XOR)
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # e.g. x = 1 y = 4
        # bitwise XOR
        # print(x^y)
        # 5
        # print(bin(x^y))
        # 0b101
        return bin(x^y).count('1')

# 5) divided by 2 and apply bit-wise XOR
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        while x or y:
            ans += (x % 2) ^ (y % 2)
            x //= 2
            y //= 2
        return ans
