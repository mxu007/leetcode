# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.

# https://leetcode.com/problems/sqrtx/description/

# 1) use binary search, notice ans is updated in case mid*mid < x
# O(log(N)) time complexit
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0: return x

        left, right = 1, x
        ans = 0
        while left <= right:
            mid = (left+right) // 2
            if mid * mid == x:
                return mid
                # ans captures the latest floor value of mid
            elif mid * mid < x:
                left = mid+1
                ans = mid
            else:
                right = mid-1
        return ans

# 2) newton's method
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0: return x
        ans = x + 1  # avoid dividing 0
        while ans*ans > x:
                ans = int(ans - (ans*ans - x)/(2*ans))  # newton's method
        return ans

# 3) binary serach use recursive approach
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def binarySearch(x, high, low):
            #print('x: ', x, ' high: ', high, ' low: ', low)
            mid = (low+high) // 2
            #print('mid', mid)
            if low <= high:
                if mid**2 == x:
                    print('find seqr of x: ', mid)
                    return mid
                elif mid**2 > x:
                    return binarySearch(x, mid-1 , low)
                else:
                    return binarySearch(x, high, mid+1)
            return mid

        if x == 0 or x == 1: return x
        return binarySearch(x, x, 0)
