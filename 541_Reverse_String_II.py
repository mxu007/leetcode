# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

# https://leetcode.com/problems/reverse-string-ii/description/

# 1) elegant solution using alternating factor d
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        # alternating d for reverse and non-reverse grou
        d=-1
        # iterate the input s with k interval
        for i in range(0, len(s), k):
            # use min to take care case at end of string
            result += s[i:min((i+k),len(s))][::d]
            # alternate value of d
            d *= -1
        return result

# 2) convention approach to iterate the list
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # get input list length
        length = len(s)
        i = 0
        result = ""

        # iterate until length becomes 0
        while (length > 0):
            # case where less than k char left
            if length < k:
                result += s[2*k*i:][::-1]
                return result
            # case where between k and 2k left
            # https://stackoverflow.com/questions/30015228/reverse-a-substring-of-a-given-string
            elif k < length < 2*k:
                result = result + s[2*k*i:2*k*i+k][::-1] + s[2*k*i+k:]
                return result
            # case where more than 2k left
            else:
                result = result + s[2*k*i:2*k*i+k][::-1] + s[2*k*i+k:2*k*i+2*k]
                length = length - 2*k
                i += 1
        return result
