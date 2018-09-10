# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# https://leetcode.com/problems/implement-strstr/description/

# 1) python built-in find()
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: return 0
        return haystack.find(needle)

# 2) python built-in index
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: return 0
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
# 3) python re.search
import re
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: return 0
        if re.search(needle,haystack):
            return re.search(needle,haystack).start()
        else:
            return -1

# linear search, O(N) time complexity
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: return 0

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
