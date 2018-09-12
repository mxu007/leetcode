# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

# https://leetcode.com/problems/valid-palindrome/description/

# 1) strip off non-alphanumerical characters, and two pointers, O(N)
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([i.lower() for i in s if i.isalnum()])

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1

        return True

# 2) use re.sub and reverse a string, O(N) time
import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub('', s).lower()
        #print(s)
        return s == s[::-1]

# 3) directly use two pointers
class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left +=1; right -= 1
        return True

# 4) one-line solution of 2)
class Solution:
    def isPalindrome(self, s):
        return re.compile('[^a-zA-Z0-9]').sub('', s).lower() == re.compile('[^a-zA-Z0-9]').sub('', s).lower()[::-1]
