# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

# https://leetcode.com/problems/longest-palindrome/description/

# 1) appraoch use set to count number of character with single occurence
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create a set
        odd_set = set()
        # only keep char with odd number of occurence
        for char in s:
            odd_set.add(char) if char not in odd_set else odd_set.remove(char)
        # length of odd_set indicates number of char we cannot use for palindrome
        return len(s)-len(odd_set)+1 if len(odd_set) > 1 else len(s)


# 2) use python collection, counters and values
# collections.Counters() returns a dictionary
# https://docs.python.org/3/library/collections.html#collections.Counter
import collections
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # get number of characters with odd number of occurence
        num_odds = (sum([v%2==1 for v in collections.Counter(s).values()]))
        return len(s) - num_odds + int(num_odds > 0)
