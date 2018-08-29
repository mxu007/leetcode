# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false

# https://leetcode.com/problems/valid-perfect-square/description/

# 1) iterative approach
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while (num // i >= i):
            if num / i == i and num % i == 0: return True
            i += 1

        return False

# 2) use power
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return isinstance(num**0.5, int)

# 3) Newton's method, log2(N) time complexity, as divided by 2 each time
# https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r*r > num:
            r = (r + num/r) // 2
        return r*r == num

# 4) Binary search, log(N) time complexity
class Solution(object):
    def isPerfectSquare(self, num):
        left = 0
        right = num

        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False
