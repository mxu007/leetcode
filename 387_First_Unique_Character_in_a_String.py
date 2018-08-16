# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase lett


# https://leetcode.com/problems/first-unique-character-in-a-string/description/


# use OrderedDict from collections
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # init dictionary to store letter-count pair
        letter_count = collections.OrderedDict()
        j = 0

        # iterate the string to construct letter-count pairs
        for letter in str(s):
            letter_count[letter] = letter_count.get(letter,0) + 1

        # find first letter with count 1
        for letter, count in letter_count.iteritems():
            if count == 1:
                return s.find(letter)

        # return -1 if not found
        return -1

# use the default python dictionary
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # init dictionary to store letter-count pair
        letter_count = {}
        j = 0

        # iterate the string to construct letter-count pairs
        for letter in str(s):
            letter_count[letter] = letter_count.get(letter,0) + 1

        # find first letter with count 1
        for i in range(0,len(s)):
            if letter_count[s[i]] == 1:
                return i

        # return -1 if not found
        return -1
