# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

# https://leetcode.com/problems/pascals-triangle/description/

# 1) using nested list
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # construct first two levels
        results = [[1],[1,1]]

        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return results

        # left and right elements of each row always equal to one
        for i in range(2,numRows):
            result = [None] * (i+1)
            result[0], result[-1] = 1, 1
            for j in range(1,len(result)-1):
                result[j] = results[i-1][j-1] + results[i-1][j]
            results.append(result)

        return(results)

# 2) more concise approach
class Solution:
    def generate(self, numRows):
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
