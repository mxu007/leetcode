# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:

# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:

# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:

# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

https://leetcode.com/problems/word-pattern/description/

# 1) use dictionary, O(N) time complexiy
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != len(str.split()): return False
        str = str.split()

        mapping = {}
        for i,char in enumerate(pattern):
            if char not in mapping and str[i] not in mapping.values():
                mapping[char] = str[i]
            elif char not in mapping and str[i] in mapping.values():
                return False
            else:
                if mapping[char] != str[i]: return False
        return True

# 2) use map function, # map(fun,iter) returns a iterator in python 3
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        # https://www.geeksforgeeks.org/python-map-function/
        # find is only available for strings where as index is available for lists, tuples and strings
        return list(map(s.find, s)) == list(map(t.index, t))

# 3) use set and set length
class Solution:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
