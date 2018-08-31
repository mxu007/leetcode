
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# Example 1:

# n = 5

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤

# Because the 3rd row is incomplete, we return 2.
# Example 2:

# n = 8

# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤

# Because the 4th row is incomplete, we return 3.

# https://leetcode.com/problems/arranging-coins/description/

# 1) iteartive approach, O(N) time complexity
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return n
        elif n == 1: return n

        i = 1
        while((1+i)*i//2 <= n):
            i += 1

        return i-1

# 2) use mathematical operations
# https://math.stackexchange.com/questions/1417579/largest-triangular-number-less-than-a-given-natural-number

import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.floor((-1+(8*n+1)**0.5)/2))


# 3) binary search, O(log(N)) time complexity
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high, ans = 1, n, 0
        while low <= high:
            mid = low + (high-low)//2

            # because we are looking for the closest integer to the triangle number
            if mid*(mid+1) <=2*n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

