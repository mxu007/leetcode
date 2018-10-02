# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

# 1) use join and string.split() function, O(N) time where N is no.of word in s
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(word[::-1] for word in s.split())


# 2) use map function
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(map(lambda x: x[::-1], s.split()))


# 3) convention approach
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        result = []
        for word in s:
            result.append(word[::-1]+' ')
        return ''.join(result)[:-1]


# 4) double reverse, first reverse flips the whole string sequence
# the second reverse restore the word sequence
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # print(s[::-1])
        # tsetnoc edoCteeL ekat s'teL
        # print(s[::-1].split(' '))
        # ['tsetnoc', 'edoCteeL', 'ekat', "s'teL"]
        # print(s[::-1].split(' ')[::-1])
        # ["s'teL", 'ekat', 'edoCteeL', 'tsetnoc']

        return ' '.join(s[::-1].split(' ')[::-1])

