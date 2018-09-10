# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.

# https://leetcode.com/problems/can-place-flowers/description/

# 1) iterate the list, O(N) time complexity, O(N) space
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n > (len(flowerbed) - sum(flowerbed)): return False
        if n == 0: return True
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return n == 1

        count, i = 0, 0
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i], count = 1, count + 1
            elif i == len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i], count = 1, count + 1
            else:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                #print(flowerbed)
                    flowerbed[i], count = 1, count + 1
                #print(flowerbed, count)

        return n <= count

# 2) more concise code of 1)
# i == 0 and i == len(flowerbed)-1 must preceed flowerbed[i-1]==0 and flowerbed[i+1]==0 to prevent out of list index error
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n > (len(flowerbed) - sum(flowerbed)): return False
        if n == 0: return True
        if len(flowerbed) == 1:
            return n == 1 and flowerbed[0]==0

        count, i = 0, 0
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0)) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i], count = 1, count + 1
        return n <= count

# 3) stop checking when counter equals n
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n > (len(flowerbed) - sum(flowerbed)): return False
        if n == 0: return True
        if len(flowerbed) == 1:
            return n == 1 and flowerbed[0]==0

        count, i = 0, 0
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0)) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i], count = 1, count + 1
                if n == count: return True

        return False

# 4) append additional 0 to the head and tails, easy to handle in the for loop
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0: return True
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0: return True

        return False

# 5) change input list to string and replace patterns
# have to handle the patterns as 010, (10 or 01) and 00
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ss = ''.join(map(str,flowerbed))
        print(ss)
        s = ss.replace('010', 'foo').replace('10', 'ba').replace('01', 'ar').replace('00', '0^')
        print(s)
        return s.count('0') >= n
