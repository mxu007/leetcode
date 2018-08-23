# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example:

# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# https://leetcode.com/problems/happy-number/description/

# 1) detect cycle using list
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # store all generated numbers in list results
        results = [n]
        # store temporary generated numbers
        transform = n

        while results[-1] != 1:
            transform = sum([int(digit)**2 for digit in str(transform)])
            # if a newly generated number was generated before, return false as this
            # number cannot be a happy number
            if transform in results:
                return False
            results.append(transform)
        # while loop ends, return True, happy number found
        return True

# 2) detect cycle using Floyd's cycle detection algo
# Floyd's tortoise and the hare algorithm moves two pointers at different speeds through the sequence of values until they both point to equal values
# https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # function to calculate sum of digit square
        def square_sum_digits(n):
            return sum([int(digit)**2 for digit in str(n)])

        # first iteration
        slow_pt, fast_pt = square_sum_digits(n), square_sum_digits(square_sum_digits(n))
        # loop till cycle happens
        while(fast_pt != slow_pt):
            slow_pt = square_sum_digits(slow_pt)
            fast_pt = square_sum_digits(square_sum_digits(fast_pt))

        return True if square_sum_digits(slow_pt) == 1 else False
}
