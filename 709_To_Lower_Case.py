# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"
# Example 3:

# Input: "LOVELY"
# Output: "lovely"

# https://leetcode.com/problems/to-lower-case/description/

# 1) O(N) time, O(N) space where N is no.of character of the input string
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        output = ''

        for char in str:
            if (65 <= ord(char) <= 90):
                output += chr(ord(char)+32)
            else:
                output += char
        return output


# 2) built-in lower function
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


# 3) variant of 1)
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        l = list(str)
        diff = ord('A') - ord('a')
        for i in range(len(str)):
            if l[i] in upper:
                l[i] = chr(ord(l[i]) - diff)
        return "".join(l)

# 4) create upper-lower mapping using ascii_uppercase and ascii_lowercase
import string
class Solution():
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        mappings = dict(zip(string.ascii_uppercase, string.ascii_lowercase))

        output = ''
        for char in str:
            if char in mappings:
                output += mappings[char]
            else:
                output += char
        return output


# 1) one-liner of 1)
return "".join([(chr(ord(s)+32) if (65<=ord(s)<=90) else s) for s in str])


