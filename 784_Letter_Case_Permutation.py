# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]
# Note:

# S will be a string with length at most 12.
# S will consist only of letters or digits.

# https://leetcode.com/problems/letter-case-permutation/description/

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        # init result list
        result = ['']

        # iterate each char in S, handle case where character is or not an alphabetical char
        for s in S:
            if s.isalpha():
                result = [i+j for i in result for j in [s.upper(), s.lower()]]
            else:
                result = [i+s for i in result]

        return result
