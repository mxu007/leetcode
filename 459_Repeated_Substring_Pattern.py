# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



# Example 1:

# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# Example 2:

# Input: "aba"
# Output: False
# Example 3:

# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

# https://leetcode.com/problems/repeated-substring-pattern/description/

# 1) iterate all the possible substring, O(N^2)
# i represent the length of substring
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)):
            if len(s) % i != 0:
                continue
            elif all(s[:i] == x for x in (s[j:j+i] for j in range(0,len(s),i))):
                return True

        return False

# 2) improved iteration
# i represents the length of substring
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        i = 2

        while n//i > 0:
            if s[:n//i] * i == s:
                return True
            i += 1

        return False

# 3) iteartion using any
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        return any(n // i * s[:i] == s
                   for i in range(1, n)
                   if n % i == 0)

