# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
# Note:
# You may assume both s and t have the same length.

# https://leetcode.com/problems/isomorphic-strings/description/

# 1) use two dictionary to check mapping, inconsitent mapping encountered then return False
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        iso_dict_s = {}
        iso_dict_t = {}
        for i in range(len(s)):
            if s[i] not in iso_dict_s and t[i] not in iso_dict_t:
                    iso_dict_s[s[i]] = t[i]
                    iso_dict_t[t[i]] = s[i]
            else:
                if s[i] in iso_dict_s and iso_dict_s[s[i]] != t[i] : return False
                if t[i] in iso_dict_t and iso_dict_t[t[i]] != s[i]: return False

        return True


# 2) simplified version of using only one dictionary
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        memo = {}

        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False

        for a, b in zip(s, t):
            print(a,b)
            if a not in memo:
                memo[a] = b
            elif b != memo[a]:
                return False
        return True

# 3) another single dictionary solution
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        iso_dict = {}
        for i in range(len(s)):
            if s[i] in iso_dict:
                if t[i] != iso_dict[s[i]]:
                    return False
            elif t[i] in iso_dict.values():
                return False
            else:
                iso_dict[s[i]] = t[i]
        return True



