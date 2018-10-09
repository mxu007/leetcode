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


# 5) single-pass, for each letter, search to left and search to right
# O(N^2) time due to the search at each index
class Solution:
    def shortestToChar(self, S, C):
        result = [0] * len(S)
        for i in range(len(S)):
            if S[i] != C:
                left_dist = S[:i+1][::-1].find(C)
                right_dist = S[i:].find(C)
                if left_dist > 0  and right_dist > 0 :
                    result[i] = min(left_dist,right_dist)
                else:
                    result[i] = left_dist if left_dist > 0 else right_dist
        return result

# 6) variant of 5), more compact if else logic
class Solution:
    def shortestToChar(self, S, C):
        result = [0] * len(S)
        for i in range(len(S)):
            if S[i] != C:
                left_dist = S[:i+1][::-1].find(C)
                right_dist = S[i:].find(C)
                result[i] = min(left_dist,right_dist) if (left_dist*right_dist > 0) else left_dist if left_dist > 0 else right_dist
        return result

# 7) variant of 3), two pointers travel from either left to right or right to left
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        i, j = 0, len(S) - 1
        left, right = None, None
        result = [float('inf')] * len(S)
        while i < len(S) and j >= 0:
            if S[i] == C: right = i
            if right != None: result[i] = min(result[i], i - right)
            if S[j] == C: left = j
            if left != None: result[j] = min(result[j], left - j)
            i += 1; j -= 1
        return result

# 8) dynamic programming, O(N) but 3-passes, 1st pass to get target indices of C
# 2nd pass move from left to right, 3rd pass move from right to left, similar to 3), 4), 7)
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        dp = [len(S)] * len(S)

        for i, s in enumerate(S):
            if s==C: dp[i] = 0

        for i in range(1,len(S)):
            dp[i] = min(dp[i], dp[i-1]+1)

        for j in range(len(S)-2, -1, -1):
            dp[j] = min(dp[j], dp[j+1]+1)

        return dp
