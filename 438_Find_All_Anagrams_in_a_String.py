# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

# 1) workable but bad time complexity using collections.Counter
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_count, p_len  = Counter([char for char in p]), len(p)
        result = []
        for i in range(len(s)-len(p)+1):
            if Counter( char for char in s[i:i+p_len]) == p_count:
                result.append(i)
        return result


# 2) sliding windowe and collection.Counter
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        if len(s) == 0 or len(p) == 0 or len(s) < len(p):   return []
        pDic = Counter(p)
        # initial sliding window is length of p minus 1
        sDic = Counter(s[:len(p)-1])
        result = []
        for endIndex in range(len(p)-1,len(s)):
            startIndex = endIndex - len(p)+1 #
            newAddLetter = s[endIndex]
            sDic[newAddLetter] += 1
            if pDic == sDic:
                result.append(startIndex)
            headLetter = s[startIndex]
            sDic[headLetter] -= 1
            # remove from Counter if count reaches 0, unnecessary
            if sDic[headLetter] == 0:
                del sDic[headLetter]
        return result
