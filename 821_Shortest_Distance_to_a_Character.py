# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


# Note:

# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.

# https://leetcode.com/problems/shortest-distance-to-a-character/description/

# 1) two-pass approach, O(NM) time where N is no.of letters in string S and N is no.of times C occur in S
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
            results.append(min((abs(x-i) for x in target_pos)))

        return results

# 2) simplified version of 1)
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        target_pos = [i for i, char in enumerate(S) if char == C]
        return [min(abs(j-i) for i in target_pos) for j in range(len(S))]

# 3) loop twice on string S: left to right and then back from right to left
# O(N) time complexy
# First forward pass to find shortest distance to target character on left.
# Second backward pass to find shortest distance to target character on the right
class Solution:
    def shortestToChar(self, S, C):
        n = len(S)
        res = [n] * n
        pos = -n
        for i in list(range(n)) + list(range(n)[::-1]):
            if(S[i] == C):  pos = i
            res[i] = min(res[i], abs(i - pos))
        return res


# 4) variant of 3)
# First forward pass to find shortest distance to target character on left.
# Second backward pass to find shortest distance to target character on the right
class Solution:
    def shortestToChar(self, S, C):
        n = len(S)
        res = [0 if c == C else n for c in S]
        for i in range(n - 1): res[i + 1] = min(res[i + 1], res[i] + 1)
        for i in range(n - 1)[::-1]: res[i] = min(res[i], res[i + 1] + 1)
        return res
