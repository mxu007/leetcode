# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]
# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?

# https://leetcode.com/problems/pascals-triangle-ii/description/

# 1) use two list prev and curr to iterate thru rows
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev = [1,1]

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return prev

        for i in range(2,rowIndex+1):
            curr = [None] * (i+1)
            curr[0], curr[-1] = 1, 1
            for j in range(1,i):
                curr[j] = prev[j-1] + prev[j]
            prev = curr

        return prev

# 2) use double layer list to construct, return the index layer
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal[rowIndex]


# 3) mathematical operation, O(N) space only
import math
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [None] * (rowIndex+1)

        def CombFunc(a,b):
            return math.factorial(a) / (math.factorial(b) * math.factorial(a-b))

        for i in range(0,rowIndex+1):
            if i <= (rowIndex+1)//2:
                result[i] = CombFunc(rowIndex,i)
            else:
                result[i] = result[rowIndex-i]

        return result

# 4) single list, double layer for loops
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return [1]
        result = [0] * (rowIndex + 1)
        result[0] = 1
        for j in range(1, rowIndex+1):
            for i in range(j, 0, -1):
                result[i] = result[i-1] + result[i]
        return result

