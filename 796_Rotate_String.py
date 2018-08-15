# We are given two strings, A and B.

# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true

# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# Note:

# A and B will have length at most 100.

# https://leetcode.com/problems/rotate-string/description/

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # case where A and B are both empty
        if (A =="" and B ==""):
            return True
        # create all the combination of A rotations as a list
        else:
            shift_A = list( str(A[i:]+A[:i]) for i in range(0,len(A)))
            return (B in shift_A)
