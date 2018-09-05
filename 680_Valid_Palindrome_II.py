# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

# https://leetcode.com/problems/valid-palindrome-ii/description/

#1) brute force solution, fails time complexity
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check_Palindrome(s):
            if len(s) % 2 == 0 :
                if s[:len(s)//2] == s[len(s)//2:][::-1]:
                    return True
            else:
                if s[:len(s)//2] == s[len(s)//2+1:][::-1]:
                    return True
            return False

        if check_Palindrome(s): return True
        else:
            for i in range(len(s)):
                s_del = s[:i] + s[i+1:]
                if check_Palindrome(s_del): return True

        return False

# 2) left and right pointers, O(N) space and O(N) time complexity
# move left and right pointer to the middle, if values at two pointers differ, we may
# shift left by 1L s[left:right] or shift right by 1: s[left+1:right+1]
# check the remaining shifted string is palindrome as palindrome is the same regardless read from left or read from right [::-1]
class Solution():
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True


# 3) similar approach as above with more concise code
class Solution():
    def validPalindrome(self, s):
            i = 0
            while i < len(s) / 2 and s[i] == s[-(i + 1)]: i += 1
            s = s[i:len(s) - i]
            # shift 1 to left or shift 1 to right
            return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]

