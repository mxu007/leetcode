# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:

# Can you solve it in O(N) time and O(1) space?

# https://leetcode.com/problems/backspace-string-compare/description/

# 1) O(M+N) time and O)1) space using generate
class Solution:
    def backspaceCompare(self, S, T):
        # generator function
        def generate_string(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        # all return true if all the iterables are true
        # To do this, you can use itertools.zip_longest().
        # This function accepts any number of iterables as arguments and a fillvalue keyword argument that defaults to None
        return all(x == y for x, y in itertools.zip_longest(generate_string(S), generate_string(T)))


# 2) O(M+N) time but O(M+N) space
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # init two list
        output_S, output_T = [], []

        # iterate S
        for s in S:
            if(len(output_S)>0 and s == "#"):
                output_S.pop()
            elif (s != "#"):
                output_S.append(s)
        # iterate T
        for t in T:
            if(len(output_T)>0 and t == "#"):
                output_T.pop()
            elif (t != "#"):
                output_T.append(t)
        # check if equal
        return output_S==output_T

