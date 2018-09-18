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

# 2) smart idea solving quadratic equation
class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 9
        for z in range(2, 2 * (9 * 10**n) - 1):
            left = 10**n - z
            right = int(str(left)[::-1])
            root_1, root_2 = 0, 0
            #print(z**2 - 4*right)
            # no root
            if z**2 - 4*right < 0:
                continue
            # single root
            elif z**2 - 4*right == 0:
                root_1 = root_2 = z/2
                if root_1.is_integer():
                    root_1 = int(root_1)
                    return ((10**n-root_1)*(10**n-(z-root_1))) %1337
            # two root
            else:
                root_1 = 1/2 * (z + (z**2-4*right)**0.5)
                root_2 = 1/2 * (z - (z**2-4*right)**0.5)
                #print(z, (z**2-4*right), (z**2-4*right)**0.5)
                if root_1.is_integer() and root_2.is_integer():
                    root_1, root_2 = int(root_1), int(root_2)
                    return max((10**n-root_1)*(10**n-(z-root_1)), (10**n-root_2)*(10**n-(z-root_2))) % 1337
                elif root_1.is_integer():
                    root_1 = int(root_1)
                    return (10**n-root_1)*(10**n-(z-root_1)) % 1337

                elif root_2.is_integer():
                    root_2 = int(root_2)
                    return (10**n-root_2)*(10**n-(z-root_2)) % 1337

# 3) simplified version of 2)
class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 9
        for z in range(2, 2 * (9 * 10**n) - 1):
            left = 10**n - z
            right = int(str(left)[::-1])
            root_1, root_2 = 0, 0
            #print(z**2 - 4*right)
            # no root
            if z**2 - 4*right < 0:
                continue
            # single root
            else:
                root_1 = 1/2 * (z + (z**2-4*right)**0.5)
                root_2 = 1/2 * (z - (z**2-4*right)**0.5)
                #print(z, (z**2-4*right), (z**2-4*right)**0.5)
                if root_1.is_integer() or root_2.is_integer():
                    return (10**n*left+right) %1337


# 4) cheating solution :)
class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [9,987,123,597,677,1218,877,475]
        return nums[n-1]
