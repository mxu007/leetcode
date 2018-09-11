# Reverse bits of a given 32 bits unsigned integer.

# Example:

# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
#              return 964176192 represented in binary as 00111001011110000010100101000000.
# Follow up:
# If this function is called many times, how would you optimize it?

# https://leetcode.com/problems/reverse-bits/description/

# 1) use python format()
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # get binary
        n = "{:032b}".format(n)
        # reverse and convert back
        return int(n[::-1],2)

# 2) use bin() and zfill()
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # get binary
        n = bin(n)[2:].zfill(32)
        # reverse and convert back
        return int(n[::-1],2)

# 3) use bin() and bit shift
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self,n):
        # get binary
        n = bin(n)[2:].zfill(32)
        result = 0
        for i in range(32):
            # result left shift
            result <<= 1
            if int(n[-1]) & 1:
                # can use both ^ (XOR) or | (OR)
                result = result ^ 1
            # right shift n
            n = n[:-1]
        return result

# 4) bin is not required for bit shift
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self,n):
        result = 0
        for i in range(32):
            # result left shift
            result <<= 1
            # if last bit of n is set
            if n & 1:
                result = result | 1
            # right shift n
            n >>= 1
        return result

# 5) mergesort like approach, divide and conquer
"""
    Divide and Conquer!  Someway like merge sort.
    For example, if there are 8 bit binary number abcdefgh,
    the process is as follow:
    abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
            # For python, there is no 32bit int, so we need to force it 32 bits.
            n = (n >> 16) | (n << 16) & 0xffffffff
            n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8) & 0xffffffff
            n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4) & 0xffffffff
            n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2) & 0xffffffff
            n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1) & 0xffffffff
            return n
