# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

# Please note that the string does not contain any non-printable characters.

# Example:

# Input: "Hello, my name is John"
# Output: 5

# https://leetcode.com/problems/number-of-segments-in-a-string/description/

# 1) use regex
import re
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        # \S stands for any non-white space character
        return len(re.findall(r'[\S]+', s))

# shorter version of 1)
import re
class Solution(object):
    def countSegments(self, s):
        return len(re.findall(r'[\S]+', s)) if len(s) != 0 else 0

# 2) use split into list and strip off white space (non-printable char)
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        s = s.split(" ")
        s = list(filter(lambda a: a!= '', s))
        return len(s)

# 3) use
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        l = s.split()
        return len(l)
