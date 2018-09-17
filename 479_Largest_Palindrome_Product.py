# Find the largest palindrome made from the product of two n-digit numbers.
# Since the result could be very large, you should return the largest palindrome mod 1337.

# Example:
# Input: 2

# Output: 987

# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

# Note:
# The range of n is [1,8].

# https://leetcode.com/problems/largest-palindrome-product/description/

# 1) O(n^2) time, fails the time complexity requirement
class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_Palindrome(num):
            # return str(num) == str(num)[::-1]
            # shall be more efficient than the str operation above
            number, reverse = num, 0
            while (number != 0): 
                reverse = reverse * 10 + number % 10
                number = number // 10
            return num == reverse
        
        first = 10 ** n - 1
        max_product = 0
        while first > 10 ** (n-1):
            second = first
            while second > 10 ** (n-1):
                if first * second < max_product: break    
                if is_Palindrome(first * second) and first * second > max_product:
                    max_product = first * second
                second -= 1
            first -= 1
        
        return max_product % 1337
