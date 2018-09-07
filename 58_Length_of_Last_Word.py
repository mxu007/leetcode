# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5

# https://leetcode.com/problems/length-of-last-word/description/

# 1) use split
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        print(s)
        if len(s) == 0: return 0
        else:
            return len(s[-1])
# 2) one-liner
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split(' ')[-1])

# 3) two pointers approach, in between two pointers are the last word
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = len(s)
        # slow and fast pointers
        slow = -1
        # iterate over trailing spaces
        while slow >= -ls and s[slow] == ' ':
            slow-=1
        fast = slow
        # iterate over last word
        while fast >= -ls and s[fast] != ' ':
            fast-=1
        return slow - fast
