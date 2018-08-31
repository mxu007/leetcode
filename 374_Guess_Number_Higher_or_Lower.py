# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I'll tell you whether the number is higher or lower.

# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# Example:
# n = 10, I pick 6.

# Return 6.

# https://leetcode.com/problems/guess-number-higher-or-lower/description/

# 1) recursive binary search, O(log(N)) time complexity
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binary_guess(low,high):
            mid = (low+high)//2

            if guess(mid) == -1:
                return binary_guess(low,mid)
            elif guess(mid) == 1:
                return binary_guess(mid+1,high)
            else:
                return mid

        return binary_guess(1,n)


# 2) iterative binary search, O(log(N)) time complexity
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 1,n
        while(i<=j):
            mid = (i+j)//2
            if(guess(mid)==0):
                return mid
            elif(guess(mid)==1):
                i = mid + 1
            elif(guess(mid)==-1):
                j = mid - 1
        return -1
