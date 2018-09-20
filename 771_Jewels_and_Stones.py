# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:

# Input: J = "z", S = "ZZ"
# Output: 0
# Note:
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

# https://leetcode.com/problems/jewels-and-stones/description/
# 1) one-liner
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in J for s in S)
 
# 2) use count()
 class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sum = 0
        for letter in J:
            sum += S.count(letter)
            
        return sum

# 3) use regex and re.findall
import re
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return len(re.findall("[%s]" % J, S))

# 4) use map and count
# map(fun, iter) Returns a list of the results after applying the given function 
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # print(list(map(J.count, S)))
        # [1, 1, 1, 0, 0, 0, 0]
        return sum(map(J.count, S))
        
 # 5) variant of 4)
 # map(fun, iter) Returns a list of the results after applying the given function 
 class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # print(list(map(S.count, J)))
        # [1, 2]
        return sum(map(S.count, J))
