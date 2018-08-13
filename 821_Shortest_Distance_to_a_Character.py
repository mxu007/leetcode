# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


# Note:

# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.

# https://leetcode.com/problems/shortest-distance-to-a-character/description/

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # init two empty list to store target positions of C and final results
        target_pos = []
        results = []

        # iterate first time to get position of the target character C
        for i in range(0,len(S)):
            if S[i] == C:
                target_pos.append(i)

        # iterate the second time to find the minimum distance from each element of the string
        # to the target character
        for i in range(0,len(S)):
            results.append(min( (abs(x-i) for x in target_pos)))

        return results
