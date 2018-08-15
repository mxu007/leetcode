
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # init two dictionary to store letter-count pairs
        s_dict = {}
        t_dict = {}

        # iterate thru two strings
        for letter in s:
            s_dict[letter] = s_dict.get(letter,0) + 1
        for letter in t:
            t_dict[letter] = t_dict.get(letter,0) + 1

        return(s_dict==t_dict)
