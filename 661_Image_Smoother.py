# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0

# https://leetcode.com/problems/image-smoother/description/

# 1) more compact solution
import copy
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # get number of rows and cols for the input
        i_len = len(M)
        j_len = len(M[0])

        # copy the original input list
        S = copy.deepcopy(M)

        for i in range(i_len):
            for j in range(j_len):
                neighbors = [
                    M[x][y]
                    for x in (i-1,i,i+1)
                    for y in (j-1,j,j+1)
                    if 0 <= x < i_len and 0 <= y < j_len
                ]
                S[i][j] = sum(neighbors) // len(neighbors)

        return S

# 2) modular appraoch
import copy
import math
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # copy the original input list
        S = copy.deepcopy(M)

        # function to retrive valid value and indicator; 1 indicates valid index
        def get_val(M, i,j):
            if (i>=0 and j>=0 and i<len(M) and j<len(M[0])):
                return M[i][j], 1
            else:
                return 0, 0
        # function to average all the valid 9 neighboring cells
        def sum_val(M, i,j):
            total = 0
            counter = 0
            comb_i = [i-1, i, i+1]
            comb_j = [j-1, j, j+1]
            for i in comb_i:
                for j in comb_j:
                    val, count = get_val(M,i,j)
                    total += val
                    counter += count
            return math.floor(total/counter)

        # iterate the returned list S
        for i in range(0,len(S)):
            for j in range(0,len(S[0])):
                S[i][j] = sum_val(M,i,j)

        return S
